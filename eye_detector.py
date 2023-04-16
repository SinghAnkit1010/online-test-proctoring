#from mtcnn.mtcnn import MTCNN
import cv2
import keras
from keras.models import Sequential 
from keras.layers import Dense ,Flatten ,Conv2D ,MaxPooling2D ,Dropout ,BatchNormalization ,GlobalMaxPool2D
import numpy as np
#face_detector = MTCNN()

model=Sequential([
                  Conv2D(32,3,activation='relu',kernel_initializer='he_normal',input_shape=(224,224,3)),
                  Conv2D(64,3,activation='relu',kernel_initializer='he_normal'),
                  BatchNormalization(),
                  MaxPooling2D(3),
    
                  Conv2D(128,3,activation='relu',kernel_initializer='he_normal'),
                  BatchNormalization(),
                  MaxPooling2D(3),
    
                  Conv2D(256,3,activation='relu',kernel_initializer='he_normal'),
                  BatchNormalization(),
                  MaxPooling2D(3),
    
                  Flatten(),
                  Dense(64,activation='relu',kernel_initializer='he_normal'),
                  BatchNormalization(),
                  Dropout(0.2),
                  Dense(4,activation='softmax',kernel_initializer='glorot_normal')
                  
])
model.load_weights("eye_detection.h5")
class eye_detection:
    def helper(self,face,left_eye,right_eye):
        lx,ly,lw,lh = left_eye
        x1,y1,x2,y2 = lx,ly,lx+lw,ly+lh
        leye_input = face[y1:y2,x1:x2]
        leye_input = cv2.resize(leye_input,(224,224))
        leye_input = leye_input.reshape(1,leye_input.shape[0],leye_input.shape[1],leye_input.shape[2])
        lprediction = model.predict(leye_input)
        rx,ry,rw,rh = right_eye
        x1,y1,x2,y2 = rx,ry,rx+rw,ry+rh
        reye_input = face[y1:y2,x1:x2]
        reye_input = cv2.resize(reye_input,(224,224))
        reye_input = reye_input.reshape(1,reye_input.shape[0],reye_input.shape[1],reye_input.shape[2])
        rprediction = model.predict(reye_input)
        class_names = ["close_look","left_look","right_look","forward_look"]
        lprediction = class_names[np.argmax(lprediction[0])]
        rprediction = class_names[np.argmax(rprediction[0])]
        if lprediction == "left_look" and rprediction =="left_look":
            return 1
        if lprediction == "right_look" and rprediction == "right_look":
            return 1
        else:
            return 0
    def result(self,face_detector,image):
        bbox = face_detector.detect_faces(image)[0]["box"]
        x,y,w,h = bbox
        x1,y1,x2,y2 = x,y,x+w,y+h
        face = image[y1:y2,x1:x2]
        gray = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        eye_cascade = cv2.CascadeClassifier("env\Lib\site-packages\cv2\data\haarcascade_eye.xml")
        eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
        left_eye = eyes[0]
        right_eye = eyes[1]
        return self.helper(face,left_eye,right_eye)


