import requests
import time
import sys
import os
import re
from datetime import datetime

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
	'Cookie':""})

def download_videos(host):
    offset = ''
    has_more = True

    if not os.path.exists(host):
        os.mkdir(host)
    
    # 打开txt文件准备写入视频URL
    with open(f'{host}/urls.txt', 'w') as url_file:
        while has_more:
            url = f'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?offset={offset}&host_mid={host}&timezone_offset=-480&features=itemOpusStyle'
            data = session.get(url).json()['data']
            has_more = data['has_more']
            offset = data['offset']
            items = data['items']

            for item in items:
                if item['type'] == 'DYNAMIC_TYPE_AV':
                    # 提取视频链接并写入txt文件
                    detail = item['modules']['module_dynamic']['major']['archive']
                    video_url = detail['jump_url'].replace('//', 'https://')
                    url_file.write(video_url + '\n')
                    print(video_url)  # 打印视频URL

            time.sleep(1)

if __name__ == '__main__':
    download_videos(sys.argv[1])
