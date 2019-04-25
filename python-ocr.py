import os                       # os の情報を扱うライブラリ
from PIL import Image           # 画像処理ライブラリ
import matplotlib.pyplot as plt # データプロット用ライブラリ
import numpy as np              # データ分析用ライブラリ
import pyocr                    # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform
import pyocr.builders           # OCR ラッパーライブラリ 対応OCR:Tesseract, Cuneiform
import re                       # 正規表現操作ライブラリ
import sys                      # 実行環境関連ライブラリ
 
def OneCharacterOcr(img):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    
    #################### 画像の読み込み ####################
    if not img:
        print("No input image")
        sys.exit(1)
    try:
        img = Image.open(img)
    except ValueError:
        print("Can not input image")
        sys.exit(1)

    #################### OCR読み取り ####################
    ocr_result = tool.image_to_string(
        img,
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )

    #################### 出力 ####################
    # 抽出したテキストの出力
    print(ocr_result,"\n")
    print("↓\n")

    # 数字だけを抽出したテキストの出力
    r = re.compile('^[0-9]+$')
    for x in filter(r.match, ocr_result):
        print(x)


input_image = 'IMAGE_FILE'
OneCharacterOcr(input_image)
