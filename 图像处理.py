


#反色
import cv2
src=cv2.imread("C:\\Users\\wei\\Pictures\\Saved Pictures\\apple.jpg",1)
print(src.shape)
Img=255-src
print(Img.shape)
cv2.imshow("Img",Img)
cv2.imshow("src",src)
cv2.waitKey(0)
#旋转
import os
from PIL import Image
img = Image.open('img/1.jpg')
img = img.transpose(Image.ROTATE_90)  # 将图片旋转90度
#img = img.transpose(Image.ROTATE_180)  # 将图片旋转180度
#img = img.transpose(Image.ROTATE_270)  # 将图片旋转270度
img.show("img/rotateImg.png")
#img.save("img/rotateImg.png")

#膨胀
import cv2 as cv

def dilate_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate", dst)

src = cv.imread("shufa.jpg")
cv.imshow("shufa", src)
# erode_demo(src)
dilate_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

#阈值化处理
img=cv2.imread("C:/picture/dog.jpg")
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
r,b=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
print(r)
cv2.imshow("img",img)
cv2.imshow("result",b)