#!/usr/bin/env python3
from flask import Flask, send_from_directory, render_template, redirect, abort
import os
from os import path
import json
from datetime import date

database = json.loads(open("database.json", "r").read())

def today():
    return 24
    #return (date.today() - date(year=2020, month=12, day=1)).days + 1

def get_active_windows(show_until):
    ret = {
        "backgroundImageUrl": database['backgroundImageUrl'],
        "windows": {}
    }

    for number in database['windows']:
        ret['windows'][number] = {}
        ret['windows'][number]['position'] = database['windows'][number]['position']
        if int(number) <= show_until and 'contentUrls' in database['windows'][number]:
            ret['windows'][number]['contentUrls'] = database['windows'][number]['contentUrls']

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
    data = get_active_windows(today())
    return render_template("index.html", description=json.dumps(data))


@app.route('/lucka/<number>')
def lucka(number):
    try:
        day = int(number)
        if day > today():
            return render_template('425.html')

        if day < len(database['windows']):
            lucka = database['windows'][number]
            return render_template('lucka.html', number=number, text=lucka['text'], video=lucka['video'])
    except Exception as e:
        print(e)
        pass

    abort(404)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(extra_files=extra_files, debug=True, host="0.0.0.0")
