#Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import tensorflow as tf
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# from keras.models import load_model
import os

# Create flask instance
app = Flask(__name__)


app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init():
    global graph
    graph = tf.compat.v1.get_default_graph()


def read_image(filename):
    img = tf.keras.preprocessing.image.load_img(filename, grayscale=False, target_size=(64, 64))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = img.reshape(1, 64, 64, 3)
    img = img.astype('float32')
    img = img / 255.0
    return img

@app.route("/", methods=['GET', 'POST'])
def home():

    return render_template('home.html')

@app.route("/predict", methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
            f = request.files['file']
            if f and allowed_file(f.filename):
              filename = f.filename
              file_path = os.path.join('static/images', filename)
              f.save(file_path)
              img = read_image(file_path)

              with graph.as_default():
                  model1 = tf.keras.models.load_model('ecggg.h5')
                  class_prediction = model1.predict_classes(img)
                  print(class_prediction)

              if class_prediction[0] == 0:
                product = "Left Bundle Branch Block"
              if class_prediction[0] == 1:
                product = "Normal"
              if class_prediction[0] == 2:
                product = "Premature Atrial Contraction"
              if class_prediction[0] == 3:
                product = "Premature Ventricular Contractions"
              if class_prediction[0] == 4:
                product = "Right Bundle Branch Block"
              if class_prediction[0] == 5:
                product = "Ventricular Fibrillation"
              return render_template('predict.html', product = product, user_image = file_path)


if __name__ == "__main__":
    init()
    app.run()