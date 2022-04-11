from flask import Flask

UPLOAD_FOLDER = '/Users/daiki/Desktop/VGG16/static/uploads'

app = Flask(__name__, static_folder = "static")
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
