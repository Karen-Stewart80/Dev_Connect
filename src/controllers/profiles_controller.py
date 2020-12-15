from flask import Blueprint, request, jsonify, abort
from schemas.ProfileSchema import profile_schema, profiles_schema
from models.Profiles import Profiles
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user
from models.Post import Post


profiles = Blueprint("profiles", __name__, url_prefix="/profiles")

@profiles.route("/", methods=["GET"])
def profiles_index():
    profiles = Profiles.query.all()
    return jsonify(profiles_schema.dump(profiles))

@profiles.route("/dev", methods=["GET"])
#@jwt_required
#@verify_user
def profiles_index_dev():
    #profiles = Profiles.query.all()
    #profile = Profiles.query.filter_by(username = username, user_id=user.id).all()
    profiles = db.session.query(Profiles, Post).join(Post, Profiles.profileid == Post.profile_id).all()
    #profile = profiles.filter_by(username = username, user_id=user.id).all()
    #return jsonify(profiles_schema.dump(profiles))
    #print(profiles)
    return str(profiles)

@profiles.route("/", methods=["POST"])
@jwt_required
@verify_user
def profiles_create(user=None):
    user_id=get_jwt_identity()
    profile_fields = profile_schema.load(request.json)
    profile=Profiles.query.get(user_id)

    new_user = Profiles()
    new_user.username = profile_fields["username"]
    new_user.fname = profile_fields["fname"]
    new_user.lname = profile_fields["lname"]
    new_user.account_active = profile_fields["account_active"]
    new_user.github = profile_fields["github"]
    new_user.front_end = profile_fields["front_end"]
    new_user.back_end = profile_fields["back_end"]
    new_user.full_stack = profile_fields["full_stack"]

    user.profile.append(new_user)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(profile_schema.dump(new_user))

@profiles.route("/<string:username>", methods=["GET"])
def profiles_show(username):
    #Return a single user
    profile = Profiles.query.filter_by(username = username).first()
    return jsonify(profile_schema.dump(profile))

@profiles.route("/<string:username>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def profiles_update(username, user=None):
    #Update a user
    profile = Profiles.query.filter_by(username = username, user_id=user.id)
    profile_fields = profile_schema.load(request.json)

    if profile.count() != 1:
        return abort(401, description="Unauthorised to update this user")
    profile.update(profile_fields)


    db.session.commit()

    return jsonify(profile_schema.dump(profile[0]))

@profiles.route("/<string:username>", methods=["DELETE"])
@jwt_required
@verify_user
def profiles_delete(username, user=None):
    #Delete a User
    profile = Profiles.query.filter_by(username=username, user_id=user.id).first()

    if not profile:
        return abort(400, description="Unauthorised to delete user")

    db.session.delete(profile)
    db.session.commit()

    return jsonify(profile_schema.dump(profile))
