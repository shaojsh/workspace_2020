# -*- coding:utf-8 -*-
# 代码很简单，但有两个误区：1.需要先获得授权码 2。需要收件人将你设置为白名单
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendEmail():
    from_addr = '2319898127@qq.com'  # 邮件发送账号
    to_addrs = 'shaojunshuai2019@126.com'  # 接收邮件账号
    qqCode = 'dqxcawrcqldadjef'  # 授权码（这个要填自己获取到的）
    smtp_server = 'smtp.qq.com'  # 固定写死
    smtp_port = 465  # 固定端口
    # 配置服务器
    stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    stmp.login(from_addr, qqCode)

    # 组装发送内容
    message = MIMEText('12306抢到票了！！！！', 'plain', 'utf-8')  # 发送的内容
    message['From'] = Header("Python邮件预警系统", 'utf-8')  # 发件人
    message['To'] = Header("管理员", 'utf-8')  # 收件人
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
    except Exception as e:
        print('邮件发送失败--' + str(e))
    print('邮件发送成功')
