from flask import Blueprint, request, jsonify
from app.models import db, Software

main = Blueprint('main', __name__)

@main.route('/software', methods=['GET'])
def get_software():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    software_list = Software.query.filter_by(user_id=user_id).all()
    return jsonify([software.to_dict() for software in software_list])

@main.route('/software', methods=['POST'])
def add_software():
    data = request.get_json()
    new_software = Software(
        name=data['name'],
        version=data['version'],
        license_key=data['license_key'],
        user_id=data['user_id']
    )
    db.session.add(new_software)
    db.session.commit()
    return jsonify(new_software.to_dict()), 201
