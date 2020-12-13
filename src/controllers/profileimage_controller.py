from models.ProfileImage import ProfileImage
from models.Profiles import Profiles
from schemas.ProfileImageSchema import profile_image_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

profile_images = Blueprint('profile_images', __name__, url_prefix="/profiles/<int:profile_id>/image")

@profile_images.route("/", methods=["POST"])
@jwt_required
def profile_image_create(profile_id):
    pass

@profile_images.route("/<int:id>", methods=["GET"])
def profile_image_show(profile_id, id):
    pass

@profile_images.route("/<int:id>", methods=["DELETE"])
@jwt_required
def profile_image_delete(profile_id, id):
    pass