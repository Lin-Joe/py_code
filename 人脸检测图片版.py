import cv2

# 实例化人脸分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 读取测试图片
img = cv2.imread('faces.jpg', cv2.IMREAD_COLOR)
# 将原彩色图转换成灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 开始在灰度图上检测人脸，输出是人脸区域的外接矩形框
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1)
# 遍历人脸检测结果
for (x, y, w, h) in faces:
    # 在原彩色图上画人脸矩形框
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
# 显示画好矩形框的图片
cv2.namedWindow('faces', cv2.WINDOW_AUTOSIZE)
cv2.imshow('faces', img)
# 等待退出键
cv2.waitKey(0)
# 销毁显示窗口
cv2.destroyAllWindows()
