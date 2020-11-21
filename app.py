#!/usr/bin/env python3
from flask import Flask, send_from_directory, render_template, redirect, abort
import os
from os import path

days = {
    '1': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '2': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '3': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '4': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '5': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '6': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '7': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '8': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '9': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '10': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '11': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '12': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '13': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '14': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '15': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '16': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '17': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '18': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '19': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '20': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '21': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '22': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '23': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
    '24': {'text': 'Blah blah', 'video': 'KfGiMxNqYrM'},
}

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
    return render_template('404.html', title = '404'), 404

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
    return render_template("index.html")


@app.route('/lucka/<number>')
def lucka(number):
    try:
        date = int(number)
        if date <= 24:
            return render_template('lucka.html', day_number=date, text=days[day_number]['text'], video=days[day_number]['video'])

    except:
        pass

    abort(404)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(extra_files=extra_files, debug=True, host="0.0.0.0")
