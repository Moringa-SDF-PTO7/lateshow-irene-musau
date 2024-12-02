from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, ma, Episode, Guest, Appearance
from marshmallow import ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def index():
    response_data = {
        "message": "Welcome to the Late Show API",
        "routes": {
            "/episodes": "GET all episodes",
            "/episodes/<id>": "GET a specific episode by ID",
            "/guests": "GET all guests",
            "/appearances": "POST to create a new appearance"
        }
    }
    # Return a prettified JSON response
    return app.response_class(
        response=jsonify(response_data).get_data(as_text=True),
        status=200,
        mimetype='application/json'
    )

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict(include_appearances=True))

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    
    try:
        episode = Episode.query.get(data.get('episode_id'))
        guest = Guest.query.get(data.get('guest_id'))
        
        if not episode or not guest:
            return jsonify({"errors": ["Invalid episode or guest"]}), 400
        
        new_appearance = Appearance(
            episode_id=data['episode_id'],
            guest_id=data['guest_id'],
            rating=data['rating']
        )
        
        db.session.add(new_appearance)
        db.session.commit()
        
        return jsonify(new_appearance.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5555)