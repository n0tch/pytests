import smtplib

content = 'example of email with python'
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()#connect to the server
mail.starttls()#encrypt the connection
email = 'gusoliv3ira@gmail.com'
pwd = 'password here'
mail.login(email, pwd)#gives the basic information about the acount
mail.sendmail(email,'ovatsug_soul@hotmail.com',content)
mail.close()
