#!/usr/bin/python3
# coding: utf-8
import os
from flask import Flask, flash, request, redirect

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/media/toshiba/aarre'
app.secret_key = "super secret key"

@app.route('/', methods=['GET', 'POST'])
def entry_point():
    file_list = [
        "aarre_intro.mp4",
        "aarre_1.mp4",
        "aarre_2.mp4",
        "aarre_3.mp4",
        "aarre_4.mp4",
        "aarre_5.mp4",
    ]
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:
            filename = request.form['img_path']
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_path)
            os.chmod(full_path, 0o777)
            return redirect(request.url)

    ret = '<head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head><body>'
    ret += '<ul>'
    for _file in file_list:
        ret += '<li style="margin-top: 3rem;">'
        ret += '<form action="/" method="POST" enctype=multipart/form-data>'
        ret += '<label for="img">{}: </label>'.format(_file)
        ret += '<input type="hidden" id="img_path" name="img_path" value="{}">'.format(_file)
        ret += '<input type="file" id="img" name="file" accept="video/*" onchange="form.submit()">'
        ret += '</form>'
        ret += '</li>'
    ret += '</ul>'
    ret += '</body>'
    return ret


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
