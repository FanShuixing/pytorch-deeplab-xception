import matplotlib.pyplot as plt
import os
import json
import numpy as np
import cv2
from skimage import io
from tqdm import tqdm
'''
重新制作pascal2012的分割数据，利用框的信息生成内接圆以作为新的分割label(灰度图)，输入的数据是
openbayes目标检测格式的数据
'''
def main(name,colormap,json_dir,save_dir,colormap_dict):
    with open(os.path.join(json_dir,name)) as fr:
        info=json.load(fr)
        h,w=int(info['image_height']),int(info['image_width'])
        oval_seg=np.zeros((h,w))
        double=np.zeros((h,w))
        for each_box in info['bboxes']:
            x_min=each_box['x_min']*w
            y_min=each_box['y_min']*h
            x_max=each_box['x_max']*w
            y_max=each_box['y_max']*h
    #         print(each_box)
            label=each_box['label']
            if label not in colormap_dict.keys():
                colormap_dict[label]=len(colormap_dict)
            ptCenter = (int(x_min+(x_max-x_min)/2),int(y_min+(y_max-y_min)/2))
            axesSize = (int((x_max-x_min)/2), int((y_max-y_min)/2))
            cv2.ellipse(oval_seg, ptCenter, axesSize, 0, 0, 360, colormap_dict[label], -1, 1)
            # tmp = np.zeros((h,w))
#             double += cv2.ellipse(tmp, ptCenter, axesSize, 0, 0, 360, 1, -1, 4)
#     oval_seg = cv2.Canny(oval_seg, 128, 256)
    #使用skimage.io.imsave保存图像的时候会发生像素变化
    cv2.imwrite(os.path.join(save_dir,'%s.png'%name.split('.')[0]),oval_seg)
    
#     plt.figure(figsize=(10,10))
#     plt.imshow(img)
    #将重叠部分置为背景
    # oval_seg[double==2]=0 
#     plt.imshow(oval_seg,alpha=0.5)
    
    
if __name__=='__main__':
    json_dir='/input1/labels'
    save_dir='./color_png'
    os.mkdir(save_dir)
    colormap=[ [128, 0, 0], [0, 128, 0], [128, 128, 0],
                       [0, 0, 128], [128, 0, 128], [0, 128, 128], [128, 128, 128],
                       [64, 0, 0], [192, 0, 0], [64, 128, 0], [192, 128, 0],
                       [64, 0, 128], [192, 0, 128], [64, 128, 128], [192, 128, 128],
                       [0, 64, 0], [128, 64, 0], [0, 192, 0], [128, 192, 0],
                       [0, 64, 128]]
    colormap_dict={}
    for each in tqdm(os.listdir(json_dir)):
        main(each,colormap,json_dir,save_dir,colormap_dict)