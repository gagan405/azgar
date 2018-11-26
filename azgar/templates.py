from azgar import app
from flask import request, abort

from azgar.models import Template


@app.route('/templates/', methods=['POST'])
def create_template():
    if not request.json:
        abort(400)
    app.logger.info('Request received' + str(request.json))
    template = Template.from_json(request.json)
    return "", 200


@app.route('/templates/')
def get_templates():
    template = str(Template.query.all())
    return template, 200