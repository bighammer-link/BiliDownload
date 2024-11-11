import requests
import time
import sys
import os
import re
from datetime import datetime

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
	'Cookie':"buvid4=10684C2D-592C-FCE3-1D43-8C66418F736222816-023020813-UiEok6mJRvsgjulSHRu0HA%3D%3D; DedeUserID=641878539; DedeUserID__ckMd5=8fc991436959bd64; buvid_fp_plain=undefined; theme_style=light; CURRENT_BLACKGAP=0; PVID=1; enable_web_push=DISABLE; bmg_af_switch=1; buvid3=DA447E39-29F1-B712-6154-520DFD79391F60014infoc; b_nut=1707394260; _uuid=E66E6874-D27B-B107F-DD3D-710AD3106934CE59492infoc; rpdid=|(J~RYYl|klJ0J'u~ukmu)m||; bmg_src_def_domain=i2.hdslb.com; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; header_theme_version=CLOSE; CURRENT_FNVAL=4048; home_feed_column=5; share_source_origin=copy_web; bsource=search_google; hit-dyn-v2=1; CURRENT_QUALITY=80; browser_resolution=1920-919; fingerprint=3fe91b34bc23dbc053e05027d89fb7a1; buvid_fp=3fe91b34bc23dbc053e05027d89fb7a1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzE0MTMzOTEsImlhdCI6MTczMTE1NDEzMSwicGx0IjotMX0.MYqI9xfnlUoMvhmwftaCfdvx6z43bu5g7WkYnekf9FE; bili_ticket_expires=1731413331; SESSDATA=7d7dbddd%2C1746768000%2C6b3ae%2Ab1CjCm-TR6Mnk-aBkOxfdnwtZALmSCUab4W2iOD9zVG8UX2b_rawHkxZHP6o1gDpYmrZMSVjF3ckU2VE9UOTNORXZFYXhuenhITlZDbXBLdnhWdm93WkpJVTRkSTdPUl9MN0toUnMyODBfeXN6WHd6dldxQTJlLUJBZ015U3RaSEtFOXZ4RWRmVjhBIIEC; bili_jct=a667393f48ad2b92b7188fb9f061d5d7; sid=7l4dorlc; bp_t_offset_641878539=998485458579095552; b_lsid=4EC67B62_1931B37986D"})

def download_videos(host):
    offset = ''
    has_more = True

    if not os.path.exists(host):
        os.mkdir(host)
    
    # 打开txt文件准备写入视频URL
    with open(f'{host}/video_urls.txt', 'w') as url_file:
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
