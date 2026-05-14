import cv2
#yeniden boyutlandırma
img= cv2.imread("assets/highway_test_image.jpg")

#print(img.shape)  #(1536, 2048, 3) pixel olduğunu öğrendik
# res = cv2.resize(img,(300,300))  #burada kendimiz manuel şekilde ayarladık
#res = cv2.resize(img,None,fx=1.4,)
res = cv2.resize(img,None,fx=1.4,fy=1,interpolation=cv2.INTER_CUBIC)


cv2.imshow("res",res)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()