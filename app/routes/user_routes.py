from flask import Blueprint, after_this_request
from flask import request
import uuid

from app.controllers import UserController, RecordController

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/create",methods=['POST'])
def create():
    data = request.json
    user =  UserController.create_user(str(uuid.uuid4()),data['name'],data['username'],data['email'],data['password'])
    return user

@user_blueprint.route("/dashboard", methods=['GET'])
def dashboard():
    uid = request.headers.get('uid')
    media_type = request.args.get('media_type')
    return RecordController.get_dashboard(uid,media_type)