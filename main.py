import cv2
import os
import numpy as np
import random

# ✅ 原圖路徑 & 輸出資料夾
folder_path = r"C:\Users\Owner\Desktop\論文"
output_path = os.path.join(folder_path, "processed")
os.makedirs(output_path, exist_ok=True)

valid_exts = ('.png', '.jpg', '.jpeg')
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_exts)]
sample_size = min(10, len(image_files))
random_images = random.sample(image_files, sample_size)

print(f"📂 圖片總數：{len(image_files)}，隨機選取：{sample_size} 張\n")

for filename in random_images:
    image_path = os.path.join(folder_path, filename)
    try:
        data = np.fromfile(image_path, dtype=np.uint8)
        img = cv2.imdecode(data, cv2.IMREAD_COLOR)

        if img is None:
            print(f"[⚠️ 略過] 無法讀取：{filename}")
            continue

        # ✅ 灰階 + 邊緣偵測處理
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        # ✅ 顯示處理後圖片
        print(f"[✅ 顯示與儲存] {filename}")
        cv2.imshow(f"{filename} - Edges", edges)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

        # ✅ 儲存處理後的圖片
        save_path = os.path.join(output_path, f"edge_{filename}")
        cv2.imencode('.png', edges)[1].tofile(save_path)

    except Exception as e:
        print(f"[❌ 錯誤] 讀取 {filename} 時發生錯誤：{e}")
