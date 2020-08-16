import os
import scipy.io as sio
import cv2
mat_path = r'D:\users\leognha\Desktop\607410158ML2\devkit\cars_train_annos'
mat = sio.loadmat(mat_path,struct_as_record=False)
test_image_path = r'D:\users\leognha\Desktop\607410158ML2\cars_train' #原始照片位置
crop_image_path = r'D:\users\leognha\Desktop\607410158ML2\crop_train' #裁切後照片位置

data = mat['annotations']
num = list(data.shape)[1] #取得總照片數量
for i in range(0,num):
    x1 = data[0][i].bbox_x1.astype(int)[0][0] #取得座標點
    y1 = data[0][i].bbox_y1.astype(int)[0][0]
    x2 = data[0][i].bbox_x2.astype(int)[0][0]
    y2 = data[0][i].bbox_y2.astype(int)[0][0]
    label = getattr(data[0][i],'class').astype(str)[0][0] #取得照片的label
    image_name = data[0][i].fname.astype(str)[0] #取得照片名字
    img = cv2.imread(test_image_path +'/'+ image_name) #讀進照片
    crop_img = img[y1:y2, x1:x2] #依座標剪下照片範圍
    label_file = crop_image_path + '/' + label
    if not os.path.exists(label_file):
        os.makedirs(label_file)   #若label資料夾未建立則建立
    cv2.imwrite(label_file + '/' + image_name, crop_img) #將裁切後的照片儲存到正確路徑