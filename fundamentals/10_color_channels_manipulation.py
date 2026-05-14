import cv2

resimm=cv2.imread("assets/highway_test_image.jpg")
resimm[:,:,2]=0

cv2.namedWindow("resim",cv2.WINDOW_AUTOSIZE)
cv2.imshow("resimm",resimm)

cv2.waitKey(0)
cv2.destroyAllWindows()