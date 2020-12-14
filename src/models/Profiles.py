from main import db
from models.ProfileImage import ProfileImage
from models.Post import Post

class Profiles(db.Model):
    __tablename__ = 'profiles'

    profileid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    account_active = db.Column(db.Boolean(), default = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_image = db.relationship("ProfileImage", backref="profile", uselist=False)
    post = db.relationship("Post", backref="profile", lazy="dynamic")
    github = db.Column(db.String(), nullable=False)

def __repr__(seelf):
    return f"<Profile {self.username}>"
