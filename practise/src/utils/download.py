# practise/scr/utils/download.py

import os
import requests

def download_image(url, save_dir, filename="downloaded.jpg"):
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)

    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✅ 圖片已下載並儲存至：{save_path}")
        return save_path
    else:
        raise Exception(f"❌ 下載失敗，狀態碼：{response.status_code}")
