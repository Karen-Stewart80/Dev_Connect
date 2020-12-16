from flask import Blueprint, request, jsonify, abort, render_template, url_for
from schemas.PostSchema import post_schema, posts_schema
from models.Profiles import Profiles
from main import db
from models.Users import Users
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_services import verify_user
from models.Post import Post
from sqlalchemy.sql import func, label

posts = Blueprint("post", __name__, url_prefix="/post")

@posts.route("/", methods=["GET"])
def post_index():
    post = Post.query.all()
    #return jsonify(posts_schema.dump(post))
    return render_template("home_page.html", posts= post)


@posts.route("/<string:account_active>", methods=["GET"])

def post_front_end(account_active):
    query = db.session.query(Post.account_active, label("active", func.count(Post.postid))).filter(Post.completed == False).group_by(Post.account_active).all()
    #return jsonify(posts_schema.dump(Post))
    # query = query.filter(Post.front_end == True)
    # posts = query.all()
    return jsonify(query)



@posts.route("/", methods=["POST"])
@jwt_required
@verify_user
def post_create(user=None):
    user_id=get_jwt_identity()
    post_fields = post_schema.load(request.json)
    profile=Profiles.query.get(user_id)

    new_post = Post()
    new_post.post_name = post_fields["post_name"]
    new_post.post_description = post_fields["post_description"]
    new_post.account_active = post_fields["account_active"]
    new_post.front_end = post_fields["front_end"]
    new_post.back_end = post_fields["back_end"]
    new_post.full_stack = post_fields["full_stack"]
    new_post.completed = post_fields["completed"]
    new_post.post_github = post_fields["post_github"]

    profile.post.append(new_post)

    db.session.add(new_post)
    db.session.commit()

    return jsonify(post_schema.dump(new_post))

# @profiles.route("/<string:username>", methods=["GET"])
# def profiles_show(username):
#     #Return a single user
#     profile = Profiles.query.filter_by(username = username).first()
#     return jsonify(profile_schema.dump(profile))

# @profiles.route("/<string:username>", methods=["PUT", "PATCH"])
# @jwt_required
# @verify_user
# def profiles_update(username, user=None):
#     #Update a user
#     profile = Profiles.query.filter_by(username = username, user_id=user.id)
#     profile_fields = profile_schema.load(request.json)

#     if profile.count() != 1:
#         return abort(401, description="Unauthorised to update this user")
#     profile.update(profile_fields)


#     db.session.commit()

#     return jsonify(profile_schema.dump(profile[0]))

# @profiles.route("/<string:username>", methods=["DELETE"])
# @jwt_required
# @verify_user
# def profiles_delete(username, user=None):
#     #Delete a User
#     profile = Profiles.query.filter_by(username=username, user_id=user.id).first()

#     if not profile:
#         return abort(400, description="Unauthorised to delete user")

#     db.session.delete(profile)
#     db.session.commit()

#     return jsonify(profile_schema.dump(profile))