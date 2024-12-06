from flask import jsonify
from app.models import User
from extension import db

class UserController:
    
    @staticmethod
    def create_user(uid, name, username, email, password):
        user = User(uid=uid, username=username, name=name, email=email)
        
        if user.check_existing_user(email=email):
            return jsonify({"message": "User already exists"}), 209
        else:
            user.set_password(password)
            try:
               db.session.commit()
            except:
                return jsonify({}), 500
        return jsonify({"message": "User created successfully"}), 201

        # user.set_password(password)
        # try:
        #     db.session.add(user)
        #     db.session.commit()
        # except:
        #     return jsonify({}), 500
        # return jsonify({"message": "User created successfully"}), 201