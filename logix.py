from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/accueil')
def index():
    return render_template('index.html')

@app.route('/auth')
def Authentification():
    return render_template('authentification.html')


if __name__ == '__main__':
    app.run(debug=True)