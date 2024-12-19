from flask import Blueprint, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import or_

from forms import LoginForm, RegisterForm
from models import db, User

# Blueprints
api_bp = Blueprint('api', __name__)
auth_bp = Blueprint('auth', __name__)
users_bp = Blueprint('users', __name__)
# Register Blueprints
api_bp.register_blueprint(auth_bp, url_prefix='/auth')
api_bp.register_blueprint(users_bp, url_prefix='/users')
# Auth Routes
@auth_bp.route('/login', methods=['POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = db.session.execute(db.select(User).where(or_(User.username == form.username.data, User.email == form.email.data))).scalar_one_or_none()
    if user:
      if user.check_password(form.password.data):
        login_user(user)
        return jsonify({ 'message': 'Login Successful!'}), 200
      else:
        return jsonify({ 'error': 'Incorrect password.'}), 401
    else:
      return jsonify({ 'error': 'Credentials not found.'}), 404
  else:
    return jsonify({ 'error': form.errors }), 400
@auth_bp.route('/register', methods=['POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(
      username = form.username.data,
      email = form.email.data,
      password = form.password.data
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'message': 'Registration Successful!'})
  else:
    return jsonify({ 'error': form.errors })
@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
  logout_user()
  return jsonify({'message': 'Logout Successful'})
# Users Routes
@users_bp.route('/me')
@login_required
def me():
  user = current_user()
  return user.to_dict()