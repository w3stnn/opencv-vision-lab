import cv2

from matplotlib import pyplot as plt


resim=cv2.imread("assets/highway_test_image.jpg",0) #resim aldık ve yolunu belirttik

cv2.namedWindow("Resim penceresi") #boş bir resim penceresi oluşturur


cv2.namedWindow("RESİM PENCERESİ",cv2.WINDOW_AUTOSIZE) #window_normal komutu ise kendin ayarlayabiliyorsun
#eğer göstermek istiyorsan üsttekini şunu yaz cv2.imshow("RESİM PENCERESİ",resim) 


cv2.imshow("resim penceresi",resim) #aldığımız resimini penceresinin ismi ve aldğımız resmin değişkeni


plt.imshow(resim) #Matrisi resme dönüştürür.
plt.show()          #Pencereyi ekrana getirir.


k=cv2.waitKey(0) #açılan pencerenin süresi aslında bir tuşa basmadan kapanmıyor

#cv2.destroyWindow("resim penceresi")


cv2.destroyAllWindows() #tüm pencereleri kapatır


if k==27:
        print("ESC TUSUNA BASILDI") #ess içine yazamadığımızdan böyle yapıyoruz

elif k ==ord("q"):
        print("q tusuna basıldı,resim kayıt edildi")
        cv2.imwrite("sonuc.jpg",resim) #resmi 0 değerinden dolayı siyah beyaz kayıt etti