#!/usr/bin/env python3
from flask import Flask, send_from_directory, render_template, redirect, abort
import os
from os import path

days = {
    '1': {'text': 'Vad är en jul utan julmat? Och vad är julmat utan potatis? Detta är en av många frågor vi Tenorer ofta tänker på. Låt oss därför inleda denna adventskalender med en sång till denna mest utsökta av kolhydratskällor.', 'video': 'ofKk_Etapq4'},
    '2': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '3': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '4': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '5': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '6': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '7': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '8': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '9': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '10': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '11': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '12': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '13': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '14': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '15': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '16': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '17': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '18': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '19': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '20': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '21': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '22': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '23': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
    '24': {'text': 'Blah blah', 'video': 'ofKk_Etapq4'},
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
    return render_template("index.html")


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
