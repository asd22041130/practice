# 📁 practise/scr/utils/image_viewer.py

import cv2
import ctypes

def show_image_top_right(title, img):
    """顯示圖片並將視窗移到螢幕右上角"""
    cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title, img)

    # 取得螢幕寬度
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)

    img_height, img_width = img.shape[:2]
    x = screen_width - img_width  # 最右邊
    y = 0  # 最上面

    cv2.moveWindow(title, x, y)
