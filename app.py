from flask import Flask, send_from_directory, render_template, redirect
import os
from os import path

extra_dirs = ['static']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)


app = Flask(__name__)

@app.context_processor
def inject_debug():
    return dict(debug=app.debug)

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/favicon.ico')
def favicon():
    return redirect("/static/images/favicon.ico")

@app.route('/')
def index():
    return redirect("/main")

@app.route('/<pagename>')
def page(pagename):
    pagename = "pages/{}.html".format(pagename)
    return render_template("base.html", page = pagename)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(extra_files=extra_files, debug=True, host="0.0.0.0")

