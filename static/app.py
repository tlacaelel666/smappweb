from doctest import OutputChecker
import sys
from pytube import YouTube
import os
from pydub import AudioSegmrnt
import app
from flask import Flask, redirect, url_for,
render_template, request, send_from_directory,
jsonify

app = flask(__name__)
DOWNLOAD_FODER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
os.makedirs(DOWNLOAD_FOLDER) 

@app.route('/')
def index():
 return render_template('index.html')

def create_app():
    app = flask(__name__)

    app.config['FLASK_APP'] = 'flask run'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=debug=True)
