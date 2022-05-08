from dis import dis
from operator import length_hint
from threading import Thread
import threading
from turtle import color
from mediapipe.python.solutions.hands import Hands,HAND_CONNECTIONS
import mediapipe.python.solutions.drawing_utils as utils
import cv2
from utils import distance
from moveMouse import *

hands = Hands()
# hands.

cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()#read the pixel from cam
    img_H=img.shape[0]#get the size of img
    img_W=img.shape[1]
    img=cv2.flip(img,1)#reverse the img
    if ret:
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)#process the img to get the result
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:#get hands
                # utils.draw_landmarks(img,hand_landmarks,HAND_CONNECTIONS)
                pos1_x = (hand_landmarks.landmark[4].x*img_W)
                pos1_y = (hand_landmarks.landmark[4].y*img_H)
                pos2_x = (hand_landmarks.landmark[8].x*img_W)
                pos2_y = (hand_landmarks.landmark[8].y*img_H)
                
                dis = distance(pos1_x,pos1_y,pos2_x,pos2_y)

                if(int(dis)<20):
                    click()

                cv2.putText(img,dis,(25,25),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),2)

                cv2.putText(img,'4',(int(pos1_x),int(pos1_y)),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),2)
                cv2.putText(img,'8',(int(pos2_x),int(pos2_y)),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),2)
                
                move(pos2_x,pos2_y)
        cv2.imshow('img',img)


    if cv2.waitKey(1) == 27:
        break
