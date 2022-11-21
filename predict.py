# import base64
# import numpy as np
# import io
# from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow import keras
# from tensorflow.keras.models import load_model
from keras.models import load_model
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

def get_model():
    global model
    model = load_model('CNN_1.h5')
    print(" * Model loaded!")

@app.route("/")
def home():
    
    return predict()

def predict():
    get_model()
    # message = request.get_json(force=True)
    # encoded = message['image']
    # decoded = base64.b64decode(encoded)
    emg=np.loadtxt('exampMini.csv',delimiter=',')
    emg = emg.reshape((1,4,512*7))
    out = model.predict(emg)
    type(out), out.shape
    
    # image = Image.open(io.BytesIO(decoded))
    # processed_image = preprocess_image(image, target_size=(224, 224))

    out = model.predict(emg)

    return np.array2string(out)

if __name__ == "__main__":
    app.run()
