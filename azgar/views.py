from flask import render_template_string, request
from flask_weasyprint import HTML, render_pdf
from azgar import app


@app.route('/render/pdf', methods=["POST"])
def convert_to_pdf():
    # Make a PDF straight from HTML in a string.
    content = request.json['content']
    app.logger.info("content received is " + content)
    html = render_template_string(content)
    return render_pdf(HTML(string=html))
