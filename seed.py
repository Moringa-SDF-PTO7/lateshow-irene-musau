import csv
from app import app, db
from models import Episode, Guest, Appearance

def seed_database():
    with app.app_context():
        # Clear existing data
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()

        # Hardcoded guest data (since file reading isn't working)
        guests_data = [
            {"name": "Michael J. Fox", "occupation": "actor"},
            {"name": "Sandra Bernhard", "occupation": "Comedian"},
            {"name": "Tracey Ullman", "occupation": "television actress"},
            {"name": "Gillian Anderson", "occupation": "film actress"},
            {"name": "David Alan Grier", "occupation": "actor"}
        ]

        # Create guests
        guests_dict = {}
        for guest_info in guests_data:
            guest = Guest(name=guest_info['name'], occupation=guest_info['occupation'])
            db.session.add(guest)
            guests_dict[guest_info['name']] = guest
        
        db.session.commit()

        # Hardcoded episode data
        episodes_data = [
            {"date": "1/11/99", "number": 1},
            {"date": "1/12/99", "number": 2},
            {"date": "1/13/99", "number": 3},
            {"date": "1/14/99", "number": 4},
            {"date": "1/18/99", "number": 5}
        ]

        # Create episodes and appearances
        for episode_info in episodes_data:
            episode = Episode(date=episode_info['date'], number=episode_info['number'])
            db.session.add(episode)
            
            # Optionally, create some sample appearances
            if episode_info['number'] <= len(guests_data):
                guest = guests_dict[guests_data[episode_info['number'] - 1]['name']]
                appearance = Appearance(episode=episode, guest=guest, rating=3)
                db.session.add(appearance)
        
        # Commit everything
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()