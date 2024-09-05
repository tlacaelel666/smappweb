from celery import Celery
from flask import Flask

app = celery('workers', broker='amqp://guest:guest@localhost//')

@app.task('/convert', methods=['POST'])
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

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

def create_app():
    app = Flask(__name__)
    app.config.update(
        CELERY_BROKER_URL='redis://localhost:6379/0',
        CELERY_RESULT_BACKEND='redis://localhost:6379/0')
    return app
    
