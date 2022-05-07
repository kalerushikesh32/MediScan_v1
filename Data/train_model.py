#Please check ipynb for more detailed steps

import numpy as np
import os
import PIL
import PIL.Image
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds
import pathlib
import random


dataset_folder_path = project_path + "/Dataset"               #Inside Dataset we have images in folders Noraml,COVID ... etc

normal_dataset_name = "Normal"
pneumonia_dataset_name = "Viral Pneumonia"
covid_dataset_name = "COVID"


def create_nn_model():
  model = keras.Sequential()
  model.add(layers.Flatten(input_shape=(512, 512)))
  model.add(layers.BatchNormalization())
  model.add(layers.Dense(512, activation=tf.nn.relu))
  model.add(layers.Dense(256, activation=tf.nn.relu))
  model.add(layers.Dense(128, activation=tf.nn.relu))
  model.add(layers.BatchNormalization())
  model.add(layers.Dense(3, activation=tf.nn.softmax))

  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
  return model



nn_model = create_nn_model()


data_dir = pathlib.Path(dataset_folder_path)    ## Data_dir


normal_images_paths_1 = list(data_dir.glob(normal_dataset_name + '/*'))
pneumonia_images_paths_1 = list(data_dir.glob(pneumonia_dataset_name + '/*'))
covid_images_paths_1 = list(data_dir.glob(covid_dataset_name + '/*'))


normal_images_paths = normal_images_paths_1[:500]
covid_images_paths = covid_images_paths_1[:300]
pneumonia_images_paths = pneumonia_images_paths_1[:400]


def create_images_dataframe(images_path, tag):
    items = [];
    
    for image_path in images_path:
      image = keras.preprocessing.image.load_img(
          image_path, color_mode='grayscale', target_size=(512, 512),
          interpolation='nearest'
      )

      image = keras.preprocessing.image.img_to_array(image)
      image = np.reshape(image, (512, 512))
      item = [(image, tag)]
      items = items + item

    return items



normal_dataset = create_images_dataframe(normal_images_paths, 0)
pneumonia_dataset = create_images_dataframe(pneumonia_images_paths, 1)
covid_dataset = create_images_dataframe(covid_images_paths, 2)


plt.figure(figsize=(10, 10))

for i in range(30):
  plt.subplot(6,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid('off')
  if i < 10:
    plt.imshow(pneumonia_dataset[i][0], cmap="gray")
  elif i >= 10 and i < 20:
    plt.imshow(covid_dataset[i][0], cmap="gray")
  else:
    plt.imshow(normal_dataset[i][0], cmap="gray")


complete_dataset = normal_dataset + pneumonia_dataset + covid_dataset
random.shuffle(complete_dataset)

X = [i[0] for i in complete_dataset] 
y = [i[1] for i in complete_dataset]


X_train, X_test, y_train, y_test = X[:1000], X[1000:], y[:1000], y[1000:]


X_train = np.asarray(X_train)
X_test = np.asarray(X_test)
y_train = np.asarray(y_train)
y_test = np.asarray(y_test)


nn_model.fit(X_train, y_train, epochs=16)


test_loss, test_acc = nn_model.evaluate(X_test, y_test)
print("Accuracy: ", test_acc)


#model to json
#seralize model
model_json = nn_model.to_json()
with open(project_path+"/out_5/model.json","w") as json_file:
  json_file.write(model_json)

#seralize weights
nn_model.save_weights(project_path+"/out_5/model.h5")