import cv2 
import numpy as np
def nothing(x):
    pass
img1 = cv2.imread("assets/highway_test_image.jpg")
img2 = cv2.imread("assets/curved_road_test.jpg")

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  #resimler aynı boyutta olmadığı için

# toplam = cv2.addWeighted(img1,0.8,img2,0.2,10)

# cv2.imshow("resim",toplam)
cv2.namedWindow("Harmanlama Paneli")
# Oran ayarı için trackbar (0-100 arası)
cv2.createTrackbar("Alpha", "Harmanlama Paneli", 70, 100, nothing)

while True:
    alpha = cv2.getTrackbarPos("Alpha", "Harmanlama Paneli") / 100
    beta = 1.0 - alpha
    
    # Canlı harmanlama
    sonuc = cv2.addWeighted(img1, alpha, img2, beta, 0)
    
    cv2.imshow("Harmanlama Paneli", sonuc)
    
    if cv2.waitKey(1) & 0xFF == 27: # ESC ile çıkış
        break

cv2.destroyAllWindows()

