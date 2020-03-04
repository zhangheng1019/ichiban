# 邮件模块封装函数
import smtplib
from email.mime.text import MIMEText


def send_mail(username, passwd, recv, title, content, mail_host='smtp.qq.com', port=587):
    """
    发送邮件函数，默认使用163.smtp
    :param username: 邮箱账号 xx@163.com
    :param passwd: 邮箱密码
    :param recv: 邮箱接收人地址，多个账号以逗号隔开  ['xxx@163.com', ]
    :param title: 邮件标题
    :param content: 邮件内容
    :param mail_host: 邮箱服务器
    :param port: 端口号
    :return:
    qq: mail_host='smtp.qq.com', port=587
    163: mail_host='smtp.163.com', port=25
    """
    msg = MIMEText(content)     # 邮件内容
    msg['Subject'] = title      # 邮件主题
    msg['From'] = username      # 发送者账号
    msg['To'] = ','.join(recv)            # 接收者账号列表
    try:
        smtp = smtplib.SMTP(mail_host, port=port)   # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
        smtp.login(username, passwd)                # 发送者的邮箱账号，密码
        # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        smtp.sendmail(username, recv, msg.as_string())
        smtp.quit()     # 发送完毕后退出smtp
        print('发送成功')
    except Exception as e:
        print('发送失败', e)


# email_user = 'zhangheng6cah@163.com'  # 发送者账号
# email_pwd = 'zh139891'  # 发送者密码(smtp授权码)

# email_user = '1792690192@qq.com'  # 发送者账号
# email_pwd = 'inodapsbunfaccig'  # 发送者密码(smtp授权码)
# maillist = ['zhangheng6cah@163.com']  # 接收人列表 应当使用factory.mail
# title = '产能提醒'  # 邮件标题
# content = '尊敬的：%s ，您好！贵司在 %s 接我司订单，今日距离接单日已是第 %s 天，贵厂的交货日期为：%s ，' \
#           '按照您厂的基础数据显示，产品 %s 至今的产量为：%s件。现在应有的产量为：%s 件, 下单的总订单数为：%s 件，' \
#           '还剩下：%s 件, 按照贵厂数据，预计还需要 %s 天才能完成，请妥善安排生产进度。'
# send_mail(email_user, email_pwd, maillist, title, content)
