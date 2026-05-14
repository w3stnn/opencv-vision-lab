import cv2
import numpy as np
img=cv2.imread("assets/curved_road_test.jpg")

print(img.shape) #görselin boyutunu öğrendik == (4032, 2268, 3)

rows,cols = img.shape[:2]

translation_matrix = np.float32([[1,0,50],[0,1,50]])

img_translation = cv2.warpAffine(img,translation_matrix,(cols+50,rows+50))

cv2.imshow("img",img)
cv2.imshow("img_translation",img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()