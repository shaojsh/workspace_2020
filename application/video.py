# cd /Users/apple/Downloads/scrapy/kankan
import requests

from multiprocessing import Pool


def download(i):
    url = 'http://vod.all-yoga.com.cn/4scVzMqo07EO0NkRQjoiIjyL-5E=/lnAJAoTQYOxgeHQO0vpWJheSK1HJ/000%03d.ts' % i
    print(url)
    r = requests.get(url)
    ret = r.content
    with open('./kankan/{}'.format(url[-6:]), 'wb') as f:
        f.write(ret)


if __name__ == '__main__':
    pool = Pool(20)
    for i in range(383):
        pool.apply_async(download, args=(i,))
    pool.close()
    pool.join()
