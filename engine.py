import numpy as np
import os
#import pandas as pd
import PIL
import PIL.Image
from tensorflow import keras
import pathlib
import random
from model.out_5.load import init

def detector_1(filename1):
  path_2 = os.getcwd()
  # dir_model = path_2 + "\\model\\"
  # dir1 = path_2 + "\\static\\uploads\\"       ## For Windows
  dir1 = path_2 + "/static/uploads/"            ## For Ubuntu
  # nn_model2 = keras.models.load_model(dir_model+"out" )
  nn_model2 = init()

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
