import cv2
import os
import numpy as np
import face_recognition
from PIL import Image

inputpath_real='C:/Users/XqsZX/PycharmProjects/face_liveness/videos/real.mp4'
inputpath_fake='C:/Users/XqsZX/PycharmProjects/face_liveness/videos/fake.mp4'
outputpath_real='C:/Users/XqsZX/PycharmProjects/face_liveness/videos/train/real/'
outputpath_fake='C:/Users/XqsZX/PycharmProjects/face_liveness/videos/train/fake/'


def cut_img(inputpath,outputpath,type,width,height):
    vs = cv2.VideoCapture(inputpath)
    read = 0
    while True:
        (grabbed, frame) = vs.read()
        if not grabbed:
            print('This frame is not grabbed')
            break
        read +=1

        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)

        for face_location in face_locations:
            top, right, bottom, left = face_location
            cropped= frame [top:bottom, left:right]
            img_name=outputpath+'%s_%d.png' %(type,read)
            cv2.imwrite(img_name, cropped,[int(cv2.IMWRITE_PNG_COMPRESSION), 9] )
            img = Image.open(img_name)
            new_image = img.resize((width, height), Image.BILINEAR)
            new_image.save(os.path.join(outputpath, os.path.basename(img_name)))

cut_img(inputpath_real,outputpath_real,'real',50,50)
cut_img(inputpath_fake,outputpath_fake,'fake',50,50)