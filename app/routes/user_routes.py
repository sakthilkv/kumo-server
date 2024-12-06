from flask import Blueprint
from flask import request
import uuid

from app.controllers import UserController
user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/create",methods=['POST'])
def create():
    data = request.json
    return UserController.create_user(str(uuid.uuid4()),data['name'],data['username'],data['email'],data['password'])