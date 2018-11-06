import cv2
import numpy as np
import tkinter as tk

from cv2 import WINDOW_NORMAL
from face_detection import find_faces
from show_content import male_content, female_content

ESC = 27

def start_webcam(model_gender, window_size, window_name, update_time=50):
    cv2.namedWindow(window_name, WINDOW_NORMAL)
    if window_size:
        width, height = window_size
        cv2.resizeWindow(window_name, width, height)

    video_feed = cv2.VideoCapture(0)
    video_feed.set(3, width)
    video_feed.set(4, height)
    read_value, webcam_image = video_feed.read()

    delay = 0
    init = True
    while read_value:
        read_value, webcam_image = video_feed.read()
        for normalized_face, (x, y, w, h) in find_faces(webcam_image):
          if init or delay == 0:
            init = False
            gender_prediction = model_gender.predict(normalized_face)
          if (gender_prediction[0] == 0):
              cv2.rectangle(webcam_image, (x,y), (x+w, y+h), (0,0,255), 2)
              cv2.putText(webcam_image, 'Female', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)
              if (female_content() == True):
                pass
          elif (gender_prediction[0] == 1):
              cv2.rectangle(webcam_image, (x,y), (x+w, y+h), (255,0,0), 2)
              cv2.putText(webcam_image, 'Male', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)
              if (male_content() == True):
                pass
          else:
              print('Hii')
        # delay += 1
        # delay %= 20
        cv2.imshow(window_name, webcam_image)
        key = cv2.waitKey(update_time)
        if key == ESC:
            break

    cv2.destroyWindow(window_name)


if __name__ == '__main__':
    fisher_face_gender = cv2.face.FisherFaceRecognizer_create()
    fisher_face_gender.read('models/gender_classifier_model.xml')
    window_name = "Machine Vision (press ESC to exit)"
    start_webcam(fisher_face_gender, window_size=(1280, 720), window_name=window_name, update_time=15)