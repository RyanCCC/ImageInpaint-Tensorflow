'''
对图像缩放
'''

import cv2

def img_resize(img, target_size):
    '''
    图像缩放
    '''
    image = cv2.resize(img, (target_size[0], target_size[1]))
    return image

def img_scale(img, target_size):
    '''
    图像等比例缩放
    '''
    old_size= img.shape[0:2]
    #ratio = min(float(target_size)/(old_size))
    ratio = min(float(target_size[i])/(old_size[i]) for i in range(len(old_size)))
    new_size = tuple([int(i*ratio) for i in old_size])
    img = cv2.resize(img,(new_size[1], new_size[0]))
    pad_w = target_size[1] - new_size[1]
    pad_h = target_size[0] - new_size[0]
    top,bottom = pad_h//2, pad_h-(pad_h//2)
    left,right = pad_w//2, pad_w -(pad_w//2)
    img_new = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,None,(0,0,0))
    return img_new

if __name__ == '__main__':
    img_path = './images/test_1.png'
    target_size =256, 256
    image = cv2.imread(img_path)
    image_resize = img_resize(image, target_size)
    img_border = img_scale(image, target_size)
    cv2.imshow("ori", image)
    cv2.imshow("resize", image_resize)
    cv2.imshow("border", img_border)
    cv2.waitKey()
    cv2.destroyAllWindows()