import os
import sys

from PIL import Image

input_folder = r'D:\face_liveness_detection\dataset\dataset\train\fake'  # 源文件夹，包含.png格式图片
output_folder = r'D:\face_liveness_detection\dataset\dataset\train_img\fake'  # 输出文件夹
# training_data=[]
a = []
for root, dirs, files in os.walk(input_folder):
    for filename in (x for x in files if x.endswith('.png')):
        filepath = os.path.join(root, filename)

        object_class = filename.split('.p')[0]
        a.append(object_class)
    print(a)

for i in a:
    old_path = input_folder + "\\" + str(i) + '.png'
    new_path = output_folder + "\\" + str(i) + '.jpg'
    img = Image.open(old_path)
    img.save(new_path)
