from static.workers import make_celery


app = create_app()
celery = make_celery(app)

@celery.task
def my_worker_task(data):

  pass

@app.route('/convert', methods=['POST'])
def convert_url_to_mp3(stre=None, Exception=None):
    try:
        url = request.json('url')

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '192',
                                }],
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            mp3_file = ydl.prepare_filename
            info_dict.replace('.webm', '.mp3').replace('.ma4', '.mp3')
        return send_file(mp3_file, mimetype='audio/mp3'), 200
    except Exception as e:
        return jsonify({"error": stre(e)}), 500
    return f"Processed: {data}"
