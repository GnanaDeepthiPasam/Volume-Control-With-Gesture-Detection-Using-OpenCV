import cv2
import mediapipe as mp
import math


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers() # This actually gets access to the devices whih we have
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None) # This actually gets access to the interface
volume = cast(interface, POINTER(IAudioEndpointVolume)) # Then it actually gets to the interface, which is volume interface i.e IAudioEndpointVolume


vRange=volume.GetVolumeRange() # This is going to give us the volume range
minv,maxv=vRange[0],vRange[1]


import numpy as np


mp_hands=mp.solutions.hands
draw=mp.solutions.drawing_utils
hands=mp_hands.Hands()

capture=cv2.VideoCapture(0)

while(True): 

    value,image=capture.read()

    rgbimage=cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # This returns a new frame with 'RGB' color scheme
    processed_image=hands.process(rgbimage) # It basically returns a processed image
    print(processed_image.multi_hand_landmarks)


    if(processed_image.multi_hand_landmarks):

        for i in processed_image.multi_hand_landmarks:

            for finger_id, landmark_co in enumerate(i.landmark): # This will give us every single landmark which we have and this will actually give us the fingure ID for every finger which we have and it will also give us the landmark coordinates as well

                # print(finger_id,landmark_co)

                height,width,channel=image.shape # It is going to give us the width and height of the image which we are capturing
                cx,cy=int(landmark_co.x * width), int(landmark_co.y * height)
                # print(finger_id, cx, cy)

                if(finger_id==4): # Thumb

                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED) # We are going to draw a circle around your thumb and here we are going to draw a circle on the image
                                                                        # frame which we have and we want the circle center to be the coordinate x and y and then the radius 
                                                                        # of the circle let's say '30' and then you have to specify the color (255,0,255) and then we basically
                                                                        # want to fill up the circle.
                    tpx,tpy=cx,cy

                if(finger_id==8): # Index

                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED)

                    ipx,ipy=cx,cy

                    cv2.line(image,(tpx,tpy),(ipx,ipy),(0,255,0),9) # We are drawing line between 2 circles and '9' indicates width
                    distance=math.sqrt((ipx-tpx)**2 + (ipy-tpy)**2) # We are calculating the distance between those 2 points or circles
                    print(distance)


                    v=np.interp(distance,[25,250],[minv,maxv]) # [25,250] indicates the distance between 2 fingures let's say that varies between 25 and 250
                    volume.SetMasterVolumeLevel(v, None)


            draw.draw_landmarks(image,i,mp_hands.HAND_CONNECTIONS)


    cv2.imshow('Image capture', image)

    if cv2.waitKey(1) & 0xFF==27:

        break

capture.release()
cv2.destroyAllWindows()

