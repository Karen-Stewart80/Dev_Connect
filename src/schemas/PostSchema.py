from main import ma
from models.Post import Post
from marshmallow.validate import Length
from schema.ProfileSchema import ProfileSchema

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
    
    
    email = ma.String(required=True, validate=Length(min=4))
    password = ma.String(required=True, validate=Length(min=6))

    post_name = ma.String(required=True, validate=Length(min=5))
    post_description = ma.String(required=True, validate=Length(min=5))
    account_active = ma.Boolean(required=True)
    front_end = ma.String(required=True, validate=Length(min=5))
    back_end = ma.String(required=True, validate=Length(min=5))
    full_stack = ma. String(required=True, validate=Length(min=5))
    completed = ma.Boolean(required=True)
    post_github = ma.String(required=True, validate=Length(min=5))
    profile = ma.Nested(ProfileSchema)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)