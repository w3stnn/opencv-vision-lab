import cv2

for i in dir(cv2):
    if "COLOR" in i:
        print(i)