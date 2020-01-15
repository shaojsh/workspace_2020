# encoding:utf-8
import requests
import pprint
import re


def downloadMusic(media_url, name):
    # 需要下载的音乐网址
    # media_url = 'http://audio04.dmhmusic.com/71_53_T10040589078_128_4_1_0_sdk-cpm/cn/0206/M00/90/77/ChR47F1_nqiAfD0hAD_MGBybIdk026.mp3?xcode=3d5e7bb2c40124d259ed184059d82848f7e7aef'
    # 请求服务器数据
    response = requests.get(media_url)
    # 创建文件
    f = open(name + '.mp3', 'wb')
    # 往文件里写数据
    f.write(response.content)
    f.close()


def get_api(songid):
    api_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid=' + str(
        songid) + '&from=web&_=1577494476410'
    response = requests.get(api_url)
    data = response.json()
    pprint.pprint(data)
    if data['error_code'] == 22000:
        url = data['bitrate']['file_link']
        name = data['songinfo']['album_title']
    else:
        return 0, 0
    return url, name


# url, name = get_api(313985)
# print(url, name)
# downloadMusic(url, name)

response = requests.get('http://music.taihe.com/artist/7898')
# 万能解决乱码问题
response.encoding = response.apparent_encoding
html = response.text
# print(html)
# 正则提取数据
song_ids = re.findall('href="/song/(\d+)" class="songlist-songname', html)
print(song_ids)
for songid in song_ids:
    url, name = get_api(songid)
    print(name, url)
    if name == 0 and url == 0:
        print('版权限制，歌曲id为 ' + songid + ' 无法下载')
    else:
        downloadMusic(url, name)
