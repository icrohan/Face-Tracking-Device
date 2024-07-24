import cv2
import threading
import numpy as np
import serial
import time

def send_object():
        global position
        position = "Center"
        lower_yellow = np.array([20, 50, 50])
        upper_yellow = np.array([40, 255, 255])
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_yellow, upper_yellow) 
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                # Find the largest contour
                contour = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if x + w/2 < (frame.shape[1]/2)-50:
                    position = "Left"
                elif x+w/2 > (frame.shape[1]/2)+50:
                    position = "Right"
                else:
                    position = "Center"

                # if y+ h/2 < frame.shape[1]/2:
                #     positiony = "top"
                # else:
                #     positiony = "bottom"

                cv2.putText(frame, position, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                # cv2.putText(frame, positiony, (50, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('m'):
                break
        cap.release()
        cv2.destroyAllWindows()
def send_data():
        ser = serial.Serial('COM5', 115200)
        while True:
            if position == 'Left':
                ser.write(b'Left')
            elif position == 'Right':
                ser.write(b'Right')
            else:
                ser.write(b"Center")
            data = ser.readline()
            print("Received:", data.decode())
        ser.close() 
thread1 = threading.Thread(target=send_object)
thread2 = threading.Thread(target=send_data)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Threads have finished executing.")