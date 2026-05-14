import cv2

img=cv2.imread("assets/curved_road_test.jpg")

print(img.shape) #görselin boyutunu öğrendik == (4032, 2268, 3)
#res= cv2.resize(img,(100,100))
res = cv2.resize(img,None,fx=1.4,fy=0.5,interpolation=cv2.INTER_CUBIC)

cv2.imshow("img",img)
cv2.imshow("res",res)

cv2.waitKey(0)
cv2.destroyAllWindows()