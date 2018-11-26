from azgar import db

# More details on sql-alchemy
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
from azgar.exceptions import JsonParseException


class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(64), index=True)
    template_name = db.Column(db.String(120), index=True)
    template = db.Column(db.Text)

    def __repr__(self):
        return '<Template {}>'.format(self.template_name)

    @staticmethod
    def from_json(json):
        try:
            return Template(**json)
        except KeyError:
            raise JsonParseException("Failed to parse template from given request")
