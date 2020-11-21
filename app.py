#!/usr/bin/env python3
from flask import Flask, send_from_directory, render_template, redirect, abort
import os
from os import path
import json

database = json.loads(open("database.json", "r").read())

def get_active_windows(show_until):
    ret = {
        "backgroundImageUrl": database['backgroundImageUrl'],
        "windows": {}
    }

    for number in database['windows']:
        if int(number) <= show_until:
            ret['windows'][number] = database['windows'][number]

    return ret

extra_dirs = ['static']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title = '404')

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

    data = get_active_windows(25)
    return render_template("index.html", description=json.dumps(data))


@app.route('/lucka/<number>')
def lucka(number):
    date = int(number)
    try:
        if date <= 24:
            return render_template('lucka.html', number=number, text=days[number]['text'], video=days[number]['video'])
    except:
        pass


    abort(404)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(extra_files=extra_files, debug=True, host="0.0.0.0")
