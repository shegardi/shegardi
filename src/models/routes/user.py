from flask import Blueprint, request, jsonify from src .models.user import User, db
user_bp = Blueprint ( 'user',
_name_
@user bp. route ('/users'
methods=[ 'GET' ]) def get_users () :
try:
users = User query all ()
return
jsonify( luser. to_dict() for user in
users]), 200
except Exception as e:
return jsonify({'error':
str (e)}), 500 @user_bp. route ('/users', methods=[ 'POST' ]) def create_user () :
try:
data = request. get_json ()
if not data or 'username'
not in data or 'email' not in data:
return jsonify({'error':
'Username and email are required' }) y
400
User query filter_by(username=data['
username ']).first():
return jsonify({'error' :
'Username already exists'}), 400
if
User query filter_by (email=datal ' ema
il']). first():
return jsonify( {'error':
'Email already exists'}), 400
user =
User (username=datal ' username'],
email=datal 'email'])
db. session. add (user)
db. session.commit ( )
return
jsonify (user. to_dict ()), 201 except Exception as e:
db. session.rollback()
return jsonify({'error':
str(e)}), 500
@user bp. route (' /users/ <int :user_id>', methods=[ 'GET' ] )
def get_user (user_id) :
try:
user =
User query get_or_404 (user_id)
return
jsonify (user. to_dict ()), 200
except Exception as e:
return jsonify({'error':
str (e)}), 404 @user bp. route('/users/
<int:user_id>' , methods=[ 'PUT' ])
def update_user (user_id) :
try:
user =
User query get_or_404 (user_ id)
data = request. get
_json ( )
if 'username' in data:
existing user =
User query filter by(username=data[' username ' ]).first()
if existing_user and
existing_user.id != user_id:
return
jsonify({' error': 'Username already exists'}), 400 user. username =
datal 'username' ]
if 'email' in data: existing user =
User query filter_by(email=datal ' ema il']). first()
if existing_user and
existing_user.id != user_id:
return
jsonify({'error': 'Email already exists'}), 400 user.email =
datal 'email']
db.session.commit ( )
return
jsonify (user. to_dict ()), 200
except Exception as e:
db. session.rollback()
return jsonify({'error':
str (e)}), 500
@user_bp. route('/users/
<int:user_id›', methods=[ 'DELETE' ])
def delete_user (user_id) :
try:
user =
User. query get_or_404 (user_id)
db. session. delete (user)
db.session.commit ( )
return
, 204
except Exception as e:
db. session.rollback()
return jsonify({'error':
str (e)}), 500
