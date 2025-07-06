import os

def data(filename):
    # 取得與 loader.py 同層級為基準的相對資料夾
    base_dir = os.path.dirname(__file__)  # → utils 目錄
    data_path = os.path.join(base_dir, "..", "data", filename)
    return os.path.abspath(data_path)
