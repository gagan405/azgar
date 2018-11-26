from azgar import app, db
from flask import request, abort, jsonify, Response

from azgar.models import Template


@app.route('/templates/', methods=['POST'])
def create_template():
    if not request.json:
        abort(400)
    app.logger.info('Request received' + str(request.json))
    template = Template.from_json(request.json)
    db.session.add(template)
    db.session.commit()
    resp = Response("")
    resp.headers['Location'] = request.base_url + str(template.id)
    resp.status_code = 201
    return resp


@app.route('/templates/')
def get_templates():
    template = str(Template.query.all())
    return jsonify(template), 200