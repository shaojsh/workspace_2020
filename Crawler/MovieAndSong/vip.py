import requests  # 网络请求
import re  # 爬虫
import tkinter as tk  # 画板
import webbrowser


def delete_text():
    t1.delete(0, 'end')


def bf():
    webbrowser.open(var.get() + t1.get())


# 1.确定url
url = 'http://www.91baidu.ren/jiexi/index.html'
resp = requests.get(url)
# print(resp.content.decode('utf-8')) #二进制网页源代码方法1（防止乱码）
resp.encoding = resp.apparent_encoding
response = resp.text
# print(response)
res = re.compile('<option value="(.*?)" selected')
reg = re.findall(res, response)
zero = 'https://jx.688ing.com/?search='
one = reg[0]
two = reg[1]
three = reg[2]
four = reg[3]
five = reg[4]
six = reg[5]
seven = reg[6]
egi = reg[7]
nine = reg[8]

# 画板
root = tk.Tk()
root.title('vip视频播放/百度音乐下载 【作成日：2019-12-15】—帅')
root.geometry('500x450+100+100')
l1 = tk.Label(root, text='播放接口', font=("Arial", 10))
l1.grid()
l2 = tk.Label(root, text='播放连接', font=("Arial", 10))
l2.grid(row=9, column=0)
t1 = tk.Entry(root, text='', width=50)
t1.grid(row=9, column=1)
# 消息循环
var = tk.StringVar()
# IntVar 是tkinter的一个类，可以管理单选按钮
ButtonList = tk.IntVar()
r0 = tk.Radiobutton(root, text='播放接口1（楼主推荐）', variable=var, value=zero)
r0.grid(row=0, column=1)
r1 = tk.Radiobutton(root, text='播放接口2（稳定通用）', variable=var, value=one)
r1.grid(row=1, column=1)
r2 = tk.Radiobutton(root, text='播放接口3（稳定通用）', variable=var, value=two)
r2.grid(row=2, column=1)
var.set(zero)
tk.Button(root, text='播放', font=("Arial", 10), width=8, command=bf).grid(row=11, column=1)
tk.Button(root, text='清除', font=("Arial", 10), width=8, command=delete_text).grid(row=12, column=1)

# variable=从属的“管理类” value=索引/ID
ButtonList.set(one)

root.mainloop()
