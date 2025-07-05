# practise/scr/utils/image_loader.py

import cv2

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"❌ 找不到圖片：{path}")
    return img

