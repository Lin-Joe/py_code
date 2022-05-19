
#反色、旋转、膨胀、设定不同阈值

import cv2 as cv
import os
from PIL import Image

#读取图片
src=cv.imread("face.jpg",1)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

#反色
inve= 255 - src
cv.imwrite("fanse.jpg", inve)

#旋转
rota = Image.open("facep.png")
rota = rota.transpose(Image.ROTATE_90)  # 将图片旋转90度
rota.save("xuanzhuan.png", quality=95, subsampling=0)

#膨胀
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
dst = cv.dilate(binary, kernel)
cv.imwrite("pengzhang.jpg",dst)

#阈值化处理
r,b=cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imwrite("yuzhi127.jpg",b)
r,bb=cv.threshold(gray,200,255,cv.THRESH_BINARY)
cv.imwrite("yuzhi200.jpg",bb)

cv.waitKey(0)
cv.destroyAllWindows()