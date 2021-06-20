import cv2
import dlib
import time

t = time.time()
path = "C:/Users/XqsZX/Desktop/data/try.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸分类器
detector = dlib.get_frontal_face_detector()
# 获取人脸检测器
predictor = dlib.shape_predictor(
    "C:/Users/XqsZX/Desktop/data/shape_predictor_68_face_landmarks.dat"
)

dets = detector(gray, 1)
for face in dets:
    shape = predictor(img, face)  # 寻找人脸的68个标定点
    # 遍历所有点，打印出其坐标，并圈出来
    for pt in shape.parts():
        pt_pos = (pt.x, pt.y)
        cv2.circle(img, pt_pos, 1, (0, 255, 0), 2)
    cv2.imshow("image", img)
print('所用时间为{}'.format(time.time() - t))
cv2.waitKey(0)
# cv2.destroyAllWindows()
time.sleep(5)
