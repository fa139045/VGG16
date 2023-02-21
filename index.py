import os
import main

from flask import Flask, render_template, request, redirect, flash, url_for
from app import app
from werkzeug.utils import secure_filename
from main import getPrediction
from datetime import datetime as dt

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    # .があるかのチェック&拡張子の確認
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index0.html')

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #### 現在時刻を名前として「uploads/」に保存する
            dt_now = dt.now().strftime("%Y%m%d%H%M%S%f")
            filename = dt_now + ".jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_path = "./static/uploads/" + filename
            getPrediction(filename)
            val = getPrediction(filename)

        return render_template('pred0.html', img_path=img_path, l1 = val[0], a1 = val[1], l2 = val[2], a2 = val[3], l3 = val[4], a3 = val[5], l4 = val[6], a4 = val[7], l5 = val[8], a5 = val[9])

if __name__ == "__main__":
    app.run(debug=True)
