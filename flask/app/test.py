import requests
from Classes import *
import smtplib

smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
smtpObj.starttls()
smtpObj.login('razumov.daniil@mail.ru','Yfabuf jy Dfv 99')
smtpObj.sendmail("razumov.daniil@mail.ru","razumoffdaniil@yandex.ru","кек лол")
smtpObj.quit()
