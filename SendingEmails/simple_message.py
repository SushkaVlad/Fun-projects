import smtplib

# простое email сообщение
from local_settings import EMAIL_FROM, PASSWORD, EMAIL_TO

dic_for_email = {'You love': 'films'}
msg = ''
for key, value in dic_for_email.items():
    msg = msg + key + value
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(EMAIL_FROM, PASSWORD)
smtpObj.sendmail(EMAIL_FROM, EMAIL_TO, msg.encode('utf-8'))
smtpObj.quit()

# необходимо разрешить доступ небезопасным приложениям (в почте)
# зачастую сообщение приходит в спам

