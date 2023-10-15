# -*- coding: UTF-8 -*-

import requests
import sys
import os

流浪Url: str = "https://p.sda1.dev/api/v1/upload_external_noform"

if __name__ == "__main__":
    # 获取命令行参数
    args = sys.argv
    if len(args) > 1:
        url = []
        for arg in args[1:]:
            img = arg

            # 验证图片
            if not os.path.isfile(img):
                continue
            valid_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")
            if not img.lower().endswith(valid_extensions):
                continue

            # 上传
            param = {
                "filename": os.path.basename(img)
            }
            r = requests.post(流浪Url, data=open(img, "rb"), params=param)

            if r.status_code == 200:
                _json = r.json()
                url.append(_json['data']['url'])
            else:
                print("Upload failed, please check the network connection...")
                print("It is also possible that your ip has been rejected")
                break

        for a in url:
            print(a)

    else:
        print("Please enter the image path as a parameter!")
