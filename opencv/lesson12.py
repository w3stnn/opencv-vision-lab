import cv2 
import numpy as np

img1 = cv2.imread("audi.png")
img2 = cv2.imread("mustang.png")

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))  #resimler aynı boyutta olmadığı için

toplam = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow("resim",toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()

