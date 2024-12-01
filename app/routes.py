from flask import Blueprint, jsonify, request
from . import db
from .models import Host, Show

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({'message': 'Welcome to Late Show API!'})

@main.route('/hosts', methods=['POST'])
def create_host():
    data = request.get_json()
    new_host = Host(name=data['name'])
    db.session.add(new_host)
    db.session.commit()
    return jsonify({'message': 'Host created successfully!', 'host': {'id': new_host.id, 'name': new_host.name}}), 201

# Get All Hosts
@main.route('/hosts', methods=['GET'])
def get_hosts():
    hosts = Host.query.all()
    hosts_list = [{'id': host.id, 'name': host.name} for host in hosts]
    return jsonify({'hosts': hosts_list})

# Update a Host
@main.route('/hosts/<int:id>', methods=['PUT'])
def update_host(id):
    host = Host.query.get(id)
    if not host:
        return jsonify({'error': 'Host not found'}), 404

    data = request.get_json()
    host.name = data.get('name', host.name)
    db.session.commit()
    return jsonify({'message': 'Host updated successfully!', 'host': {'id': host.id, 'name': host.name}})

# Delete a Host
@main.route('/hosts/<int:id>', methods=['DELETE'])
def delete_host(id):
    host = Host.query.get(id)
    if not host:
        return jsonify({'error': 'Host not found'}), 404

    db.session.delete(host)
    db.session.commit()
    return jsonify({'message': 'Host deleted successfully!'})

# Create a Show
@main.route('/shows', methods=['POST'])
def create_show():
    data = request.get_json()
    host = Host.query.get(data['host_id'])
    if not host:
        return jsonify({'error': 'Host not found'}), 404

    new_show = Show(title=data['title'], host=host)
    db.session.add(new_show)
    db.session.commit()
    return jsonify({'message': 'Show created successfully!', 'show': {'id': new_show.id, 'title': new_show.title, 'host_id': new_show.host_id}}), 201

# Get All Shows
@main.route('/shows', methods=['GET'])
def get_shows():
    shows = Show.query.all()
    shows_list = [{'id': show.id, 'title': show.title, 'host_id': show.host_id} for show in shows]
    return jsonify({'shows': shows_list})