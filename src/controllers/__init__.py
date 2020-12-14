from controllers.profiles_controller import profiles
from controllers.users_controller import auth
from controllers.profileimage_controller import profile_images
from controllers.post_controller import posts

registerable_controllers = [
    auth,
    profiles,
    profile_images,
    posts
]