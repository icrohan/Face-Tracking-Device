# Face-Tracking-Device
Face Tracking device using Open-CV and ESP-32

Capture video from a camera and process it with OpenCV to detect and track faces.
Send control commands to the ESP32 to control the movement of the camera or device based on the position of the detected face.
Control the motors connected to the ESP32 to follow the detected face.
Components Needed
ESP32: To control the motors and communicate with the OpenCV system.
Camera Module: ESP32-CAM or a USB camera connected to a computer running OpenCV.
Servo Motors: For controlling the movement of the camera or device.
Power Supply: For the motors and ESP32.
Computer: For running the OpenCV application.
System Architecture
OpenCV for Face Detection: The computer running OpenCV captures frames from the camera, processes them to detect faces, and determines the position of the faces in the frame.
Communication with ESP32: Based on the face's position, the OpenCV application sends control commands to the ESP32 to adjust the camera or device movement.
Servo Motor Control: The ESP32 receives the commands and drives the servo motors to follow the face.
