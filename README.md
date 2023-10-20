# Gesture Volume Control Software For Windows
## Technologies used:
Python: Programming language

OpenCV: To capture webcam input

Mediapipe: To detect, track hands

Pycaw: To control system volume on Windows

## Tools used:
Visual Studio Code

## Project description:
In this project, I create a software that will enable me to control the volume of my computer with just two fingers 
through gestures. This software captures my webcam input, detects focal points on my hand like the fingertips and joints and
allows me to find the distance between two points. To build this application, I use opencv's python module
which allows me to capture video from my web cam, frame-by-frame. After the video has been recorded, I then use 
MediaPipe which offers me a collection of machine learning models that have previously been trained and allows me 
to detect hands in a live video. Thereafter, I detect the key points on my hands to detect a gesture and find the 
distance between tips of two fingers so that I could control system volume.

Finally, I make use of pycaw on Windows to control the system volume and integrate the two things together so that 
volume could be controlled by two fingers.

## Demo Video:
https://github.com/GnanaDeepthiPasam/Volume-Control-With-Gesture-Detection-Using-OpenCV/assets/148503787/bf762d5a-962b-416d-8ea3-3bfed2644ccd


