import cv2

cam=cv2.VideoCapture("assets/highway_test_video.mp4")      #öncekinde kamerayı açmıştık bu sefer videoyu açıyoruz

while cam.isOpened(): #"Video dosyası düzgün açıldı mı?" veya "Video bitti mi?" kontrolü yapar. Video devam ettiği sürece döngü çalışır.

    ret,frame=cam.read()                             #Videodan bir sonraki kareyi (fotoğrafı) çeker.
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     #görüntüyü gri yapar

    if not ret:
        print("kameradan görüntü okunamıyor")
        break

    cv2.imshow("görüntü",frame)

    if cv2.waitKey(1) &0xFF== ord("q"):  #8bit için aynı değeri verir
        print("video kapatıldı")
        break

cam.release()                            #uygulama kapandığında kamerayı kapatmak için
cv2.destroyAllWindows()

