from flask import render_template, url_for, render_template_string, request
from flask_weasyprint import HTML, render_pdf
from azgar import app
import time

@app.route('/hello/', defaults={'name': 'World'})
@app.route('/hello/<name>/')
def hello_html(name):
    app.logger.info('Example log ... ')
    return render_template('hello.html', name=name)


@app.route('/test')
def hello_html1():
    app.logger.info('Example log ... ' + str(time.time()))
    time.sleep(0.2)
    return ""

@app.route('/hello_<name>.pdf')
def hello_pdf1(name):
    # Make a PDF from another view
    return render_pdf(url_for('hello_html', name=name))

# Alternatively, if the PDF does not have a matching HTML page:


@app.route('/hello_<name>.pdf')
def hello_pdf(name):
    # Make a PDF straight from HTML in a string.
    html = render_template('hello.html', name=name)
    return render_pdf(HTML(string=html))


@app.route('/blah', methods=["POST"])
def convert_to_pdf():
    # Make a PDF straight from HTML in a string.
    content = request.json['content']
    app.logger.info("content recieved is " + content)
    html = render_template_string(content)
    return render_pdf(HTML(string=html))
