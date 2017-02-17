#coding=utf-8


import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def _formataddr(s):
	name, addr = parseaddr(s)
	encode = Header(name,'utf-8').encode()
	if isinstance(addr,unicode):
		addr = addr.encode('utf-8')
	return formataddr(( encode, addr ))


def send_mail(u,title,content):

	u = u.strip()

	sender = ''
	smtphost = ""
	port = 25
	password = ""

	receivers = [u]
	message = MIMEText(content, 'html', 'utf-8')
	message['From'] = _formataddr(sender)
	message['To'] =  _formataddr(u)

	subject = title 
	message['Subject'] = Header(subject, 'utf-8')

	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(smtphost,port)
		smtpObj.login(sender,password)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print "邮件发送成功"
	except smtplib.SMTPException:
		print "Error: 无法发送邮件"

if __name__ == "__main__":
	send_mail("xingyue@staff.sina.com.cn","hello","Hello world")
