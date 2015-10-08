# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
python邮件发送方法
'''
import smtplib  
from email.mime.text import MIMEText

mailto_list=["liupeng3@ucweb.com"]
mail_host="mail.ucweb.com"  #设置服务器
mail_user="liupeng3"    #用户名
mail_pass="x"   #口令
mail_postfix="ucweb.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    me="liupeng3"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='UTF-8')
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False
def send_result(res_dic):
    sub = ""
    text = ""
    case_count = str(res_dic["f_count"] + res_dic["p_count"])
    if res_dic["f_count"] == 0:
        sub = "autotest all succeed"
        text = "case count:" + case_count + " pass: " + str(res_dic["p_count"]) + " fail: " + str(res_dic["f_count"])
    else:
        sub = "autotest same case error"
        text = "case count:" + case_count + " pass: " + str(res_dic["p_count"]) + " fail: " + str(res_dic["f_count"])
    send_mail(mailto_list, sub, text)
# if __name__ == '__main__':
#     if send_mail(mailto_list, sub, text):
#         print "发送成功"
#     else:
#         print "发送失败"