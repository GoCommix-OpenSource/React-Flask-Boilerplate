from flask import current_app as app, render_template

@app.route('/', methods=['GET'], defaults={'path': ''})
@app.route("/<path:path>")
def home(path):
    return render_template("index.html")