# 📁 practise/scr/main.py

import requests
import numpy as np
import cv2
from utils.image_viewer import show_image_top_right

def main():
    while True:
        # ✅ 從 picsum.photos 隨機取得一張圖片（800x800）
        url = "https://picsum.photos/800"
        response = requests.get(url)

        if response.status_code != 200:
            print("❌ 圖片下載失敗")
            continue

        # ✅ 轉為 OpenCV 可讀取格式
        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is None:
            print("❌ 解碼失敗")
            continue

        # ✅ 強制圖片為 800x800 大小（避免意外尺寸）
        resized = cv2.resize(img, (800, 800))
        print(f"✅ 顯示圖片尺寸：{resized.shape[1]}x{resized.shape[0]}")

        # ✅ 顯示圖片（視窗會出現在螢幕正中央）
        show_image_top_right("📸 隨機圖片展示", resized)

        # ✅ 等待 2 秒後自動關閉，或按 q / Esc 結束
        key = cv2.waitKey(2000)
        cv2.destroyAllWindows()

        if key == ord('q') or key == 27:
            print("🛑 使用者中止抓圖")
            break

if __name__ == "__main__":
    main()
