from pytube import YouTube
import os
from flask import Flask, redirect, url_for,
render_template, request, send_from_directory,
jsonify

app = flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    url = request.form['url']
    ydl_opts = {'format':'bestaudio'}
    with YouTubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        mp3_file = info['title']
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download('Downloads')
        file_name = f"{mp3_file}.mp3"
        return jsonify({'message':f"File download: {file_name}"})
    
@app.route('/download/<file_name>')
def download(file_name):
    return send_from_directory('Downloads', file_name)
        Downloads = 'DOWNLOAD_FOLDER'
if not os.path.exists(DOWNLOAD_FOLDER):
os.makedirs(DOWNLOAD_FOLDER) 

if __name__ == '__main__':
    app.run(debug=True)
