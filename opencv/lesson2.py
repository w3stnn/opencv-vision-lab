""" import cv2

import numpy as np

sifir= np.zeros([100,100])  #siyah 

bir=np.ones([100,100])  #beyaz

cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)

cv2.namedWindow("bir",cv2.WINDOW_NORMAL)

cv2.imshow("sifir",sifir)

cv2.imshow("bir",bir)

cv2.waitKey(0)

cv2.destroyAllWindows() """

import cv2

cam= cv2.VideoCapture(0)       #vide açmak için içindeki değer ile kamerayı seçersin

print(cam.get(3))   #kameranın genişliği
print(cam.get(4))   #kameranın yüksekliği

cam.set(3,320)
cam.set(4,240)      # 4:3 oranında 320x240 çözünürlükte oluşturur


if not cam.isOpened():
    print("kamera tanınmadı")
    exit()                      #Kameranın gerçekten açılıp açılmadığını kontrol eder.

while True:                                      #kamera açık olduğu sürece sonsuz bir döngü başlatır
    ret, frame = cam.read()                      
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Renkli BGR görüntüyü, işlem hızını artırmak için gri tonlamalı (tek kanallı) hale getirir.


    if not ret:
        print("kameradan görüntü okunamıyor")
        break

    cv2.imshow("kamera",frame)

    if cv2.waitKey(1) & 0xFF ==ord("q"):
        print("görüntü sonlandılırdı")
        break

cam.release()               #uygulama kapandığında kamerayı kapatmak için
cv2.destroyAllWindows()    