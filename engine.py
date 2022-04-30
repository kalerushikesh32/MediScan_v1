import numpy as np
import os
import pandas as pd
import PIL
import PIL.Image
from tensorflow import keras
import pathlib
import random

def detector_1(filename1):
  dir = "C:\\Users\\lenovo\\SPE\\MediScan_v2\model\\"
  dir1 = "C:\\Users\\lenovo\\SPE\\MediScan_v2\\static\\uploads\\"
  nn_model2 = keras.models.load_model(dir+"out" )

  # normal_images_paths = dir+"image\\COVID.png"
  normal_images_paths = dir1+filename1
  normal_image_test = keras.preprocessing.image.load_img(
      normal_images_paths, color_mode='grayscale', target_size=(512, 512),interpolation='nearest')
  normal_image_test = keras.preprocessing.image.img_to_array(normal_image_test)
  normal_image_test = np.reshape(normal_image_test, (512, 512))

  predict = nn_model2.predict(np.array([normal_image_test]))
  if np.argmax(predict[0]) == 0:
    return("Normal")
  elif np.argmax(predict[0]) == 1:
    return("Pneumonia")
  else:
    return("Covid")
