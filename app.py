from models import User, TokenBlocklist
from config import app, api, db
from flask_restful import Resource
from flask import make_response, session, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, get_jwt_identity
from datetime import datetime, timezone


class Home(Resource):
    def get(self):
        return make_response({"message":"Flask RESTful API by Felix"})


api.add_resource(Home, "/")

class Signup(Resource):
    def post(self):
        try:
            username = request.json.get("username")
            password = request.json.get("password")

            if not (username and password):
                return make_response({"error": "Missing credentials"}, 400)

            user = User.query.filter_by(username=username).first()

            if user:
                return {'message': "User Already Exists"}, 400

            new_user = User(username=username)
            new_user.password_hash = password

            db.session.add(new_user)
            db.session.commit()

            # create authentication for new user
            access_token = create_access_token(identity=new_user.id)

            return {
                'message': "User Registration Success",
                'access_token': access_token
            }, 201

        except Exception as e:
            return {"error": str(e)}, 500

api.add_resource(Signup, "/signup")



class Login(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User.query.filter(User.username == username).first()

        if user and user.authenticate(password):
            access_token = create_access_token(identity=user.id)
            return {
                'message': "User Login Success",
                'access_token': access_token
            }, 200
        else:
            return make_response({"error":"Invalid username or password"})


api.add_resource(Login, "/login")


@app.route("/logout", methods=["DELETE"])
@jwt_required()
def modify_token():
    try:
        token = get_jwt()
        jti = token["jti"]
        ttype = token["type"]
        user_id = get_jwt_identity()
        now = datetime.now(timezone.utc)

        existing_token = TokenBlocklist.query.filter_by(jti=jti).first()

        if existing_token:
            return jsonify(error="Token already revoked"), 400

        db.session.add(TokenBlocklist(jti=jti, type=ttype, created_at=now, user_id=user_id))
        db.session.commit()
        return jsonify(msg=f"{ttype.capitalize()} token successfully revoked")
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500


class Users(Resource):
    @jwt_required()
    def get(self):
        users = []

        for user in User.query.all():
            users.append(user.to_dict())

        return make_response({"users": users})


api.add_resource(Users, "/users")


if __name__ == "__main__":
    app.run(debug=True)



