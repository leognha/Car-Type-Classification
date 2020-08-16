import os
import scipy.io as sio
import cv2
mat_path = r'D:\users\leognha\Desktop\607410158ML2\devkit\cars_test_annos_withlabels'
mat = sio.loadmat(mat_path,struct_as_record=False)
test_image_path = r'D:\users\leognha\Desktop\607410158ML2\cars_test'
crop_image_path = r'D:\users\leognha\Desktop\607410158ML2\crop_test'

data = mat['annotations']
num = list(data.shape)[1]
for i in range(0,num):
    x1 = data[0][i].bbox_x1.astype(int)[0][0]
    y1 = data[0][i].bbox_y1.astype(int)[0][0]
    x2 = data[0][i].bbox_x2.astype(int)[0][0]
    y2 = data[0][i].bbox_y2.astype(int)[0][0]
    label = getattr(data[0][i],'class').astype(str)[0][0]
    image_name = data[0][i].fname.astype(str)[0]
    img = cv2.imread(test_image_path +'/'+ image_name)
    crop_img = img[y1:y2, x1:x2]
    label_file = crop_image_path + '/' + label
    if not os.path.exists(label_file):
        os.makedirs(label_file)
    cv2.imwrite(label_file + '/' + image_name, crop_img)