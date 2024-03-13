from flask import jsonify, request

from app import app, db
from app.models.user import User


@app.route("/users/", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)

    try:
        if data is None:
            return {"message": "No input data provided"}, 400

        name = data.get("name")
        email = data.get("email")

        if name is None or email is None:
            return {"message": "name and email are required"}, 400

        user = User.query.filter_by(email=email).first()
        if user:
            return {"message": f"User with email: {email} already exists"}, 400

        user = User(
            name=data.get("name"),
            email=data.get("email"),
        )

        db.session.add(user)
        db.session.commit()
        return jsonify(user), 201
    except Exception as e:
        return str(e)


@app.route("/users/", methods=["GET"])
def get_all_users():
    try:
        users = User.query.all()
        return jsonify(users), 200
    except Exception as e:
        return str(e)


@app.route("/users/<int:id>/", methods=["GET"])
def get_one_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return {"message": f"User with id: {id} not found"}, 404
        return jsonify(user), 200
    except Exception as e:
        return str(e)


@app.route("/users/<int:id>/", methods=["PATCH"])
def update_user(id):
    data: dict = request.get_json(silent=True)
    try:
        user = User.query.filter_by(id=id).first()
        if user is None:
            return {"message": f"User with id: {id} not found"}, 404

        if data is None:
            return {"message": "No input data provided"}, 400
        else:
            user.name = data.get("name") or user.name
            user.email = data.get("email") or user.email
            db.session.commit()
            return jsonify(user), 200

    except Exception as e:
        return str(e)


@app.route("/users/<int:id>/", methods=["DELETE"])
def delete_user(id):
    try:
        user = User.query.get(id)
        if user is None:
            return {"message": f"User with id: {id} not found"}, 404
        else:
            db.session.delete(user)
            db.session.commit()
            return {"message": f"User with id: {id} deleted"}, 204
    except Exception as e:
        return str(e)
