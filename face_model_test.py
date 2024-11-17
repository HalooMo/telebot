import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow import keras
from PIL import Image
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model



def SalimID(img_path):
    model = load_model(r"C:\Users\salim\GetFiles\F_model\convnet_from_scratch2.1.keras")
    res = False
    image = load_img(img_path, target_size=(640, 480))
    img = np.array(image)
    img = img / 255
    img = img.reshape(1,640,480,3)
    label = model.predict(img)
    if (label*1000-980)  > 5:
        print("This is Salim")
        print((label*1000-980))
        return True
    else:
        print("Not found")
        print((label*1000-980))
        return False
