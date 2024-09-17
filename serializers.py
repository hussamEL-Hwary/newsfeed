from marshmallow import Schema, fields, validate


class PostSchema(Schema):
    user_id = fields.Int(required=True)
    content = fields.Str(required=True, validate=validate.Length(max=255))


# Initialize the schema
post_schema = PostSchema()
