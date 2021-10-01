from flask import Flask, json, jsonify, request, render_template, url_for, redirect, send_from_directory
from werkzeug.utils import secure_filename
from app.torch_utils import transform_image, get_prediction # path_change
import os
import logging

app = Flask(__name__)

UPLOAD_FOLDER = 'app/uploads' # path_change
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(file):
    return '.' in file and file.split('.')[-1] in ['jpg', 'png', 'jpeg', 'JPG', 'JPEG']

classes = ('plane', 'car', 'bird', 'cat', 'deer',
            'dog', 'frog', 'horse', 'ship', 'truck')

@app.route("/")
def index():
    return render_template('browse_file.html', label='', imagesource='file://null')

@app.route("/", methods=['POST', 'GET']) 
def predict():
    if request.method == 'POST':
        output = ''
        image_url = ''
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image_url = url_for('uploaded_file', filename=filename)
            img_bytes = open(file_path, 'rb').read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            output = classes[prediction]
            # return '''<h1>Predicted Class: {}</h1>
            # <img src="{}" height = "224" width="224"/>'''.format(output, image_url)
            # return redirect(url_for('uploaded_file', name=filename))
    return render_template('browse_file.html', label=output, imagesource=image_url)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)