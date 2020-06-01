import numpy as np
import cv2
import serial

ser= ser = serial.Serial('COM5', 9600)

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.putText(frame,'Fuego',(x-20, y-20), font, 1,(0,0,255),1)
        #print(x)
        if x>100:
            ser.write(str('h').encode())
        else:
            ser.write(str('n').encode())

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
