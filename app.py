from .static import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def create_app():
['FLASK_APP'] = 'flask run'

if __name__ == '__main__':
    app.run(debug=True, port='$PORT')
