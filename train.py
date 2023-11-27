import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from IPython.display import display, Javascript
from base64 import b64decode
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
import seaborn as sns
from keras import models, layers, optimizers, utils, losses
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from keras.models import save_model
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import cv2  # OpenCV library for image processing
from flask import Flask, request
from tensorflow.keras.callbacks import ModelCheckpoint
import imgcompare
import math
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from keras.layers import Activation
epochs=10

train_dir = 'data/train'
val_dir = 'data/test'
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(232,232),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(232,232),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')


train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.2,
    zoom_range=0.2,
     fill_mode = 'nearest',
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

Custom_Model = Sequential()

# Step 1 - Convolution Layer
Custom_Model.add(Conv2D(32, (3, 3), input_shape=(232, 232, 1), activation='relu'))

# Step 2 - Pooling Layer
Custom_Model.add(MaxPooling2D(pool_size=(2, 2)))

# Add a second convolutional layer
Custom_Model.add(Conv2D(64, (3, 3), activation='relu'))
Custom_Model.add(MaxPooling2D(pool_size=(2, 2)))

# Add a third convolutional layer
Custom_Model.add(Conv2D(128, (3, 3), activation='relu'))
Custom_Model.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
Custom_Model.add(Flatten())

# Step 4 - Full Connection
Custom_Model.add(Dense(units=128, activation='relu'))
Custom_Model.add(Dense(units=3, activation='softmax'))  # 3 output units for 3 classes

Custom_Model.summary()

# Compile the model
Custom_Model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])


# Configure Model Checkpoint
fle_s='./Models/Custom_Model.h5'
checkpointer = ModelCheckpoint(fle_s, monitor='loss',verbose=1,save_best_only=True,
                               save_weights_only=False, mode='auto',save_freq='epoch')



'''callback_list=[checkpointer]


history = Custom_Model.fit(
    train_generator,
    steps_per_epoch=len(train_generator)//8
    ,epochs=epochs,shuffle=True,callbacks=[callback_list],
    validation_data=validation_generator,
    validation_steps=len(validation_generator)//64
)
Custom_Model.save('model.h5')'''

print("Training Completed!!")