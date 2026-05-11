import cv2 
import numpy as np


img1 = cv2.imread("opencv.png")
img2 = cv2.imread("Kizkulesi.jpg")

x,y,z = img1.shape
roi = img2[0:x,0:y]

# img1.shape
# img2.shape
# print(img1.shape,img2.shape)

img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img_gray,25,255,cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg = cv2.bitwise_and(img1,img1,mask=mask)

toplam=cv2.add(img1_bg,img2_fg)

img2[0:x,0:y]=toplam

cv2.imshow("resim6",img2)
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)

cv2.imshow("resim5",toplam)
cv2.imshow("resim4",img2_fg)
cv2.imshow("resim3",img1_bg)
cv2.imshow("resim2",mask_inv)
cv2.imshow("resim",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()