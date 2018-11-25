from azgar import db

# More details on sql-alchemy
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database


class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(64), index=True)
    template_name = db.Column(db.String(120), index=True)
    template = db.Column(db.Text)

    def __repr__(self):
        return '<Template {}>'.format(self.template_name)