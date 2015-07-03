import smtplib

if __name__ == '__main__':
	content = 'example of email with python'
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()#connect to the server
	mail.starttls()#encrypt the connection
	email = 'gusoliv3ira@gmail.com'
	pwd = '11011100'
	mail.login(email, pwd)#gives the basic information about the acount
	mail.sendmail(email,'ovatsug_soul@hotmail.com',content)
	mail.close()

