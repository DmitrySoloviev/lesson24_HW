from marshmallow import Schema, fields, validate


VALID_CMD_COMMANDS = ('filter', 'unique', 'map', 'limit', 'sort', 'regex')


class RequestSchema(Schema):
    cmd1 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD_COMMANDS))
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)

data = {
  "file_name": "apache_logs.txt",
  "cmd1": "regex",
  "value1": "images/\\w+\\.png",
  "cmd2": "sort",
  "value2": "desc"
}

data = RequestSchema().load(data)

print(type(data))

