import Adafruit_DHT
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
num= str(temperature)[:str(temperature).find('.')+2]

        
content = MIMEMultipart()
content["subject"] = "Temperature Warning Message"  #郵件標題
content["from"] = "test@mail.com"  #寄件者
content["to"] = "test@mail.com" #收件者
content.attach(MIMEText("Temperature too high greater than 25°C ,It's "+ num + "°C now"))

content1 = MIMEMultipart()
content1["subject"] = "Temperature Warning Message"  #郵件標題
content1["from"] = "test@mail.com"  #寄件者
content1["to"] = "test@mail.com" #收件者
content1.attach(MIMEText("Temperature is too low, below 18°C ,It's "+ num + "°C now"))

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("test@mail.com","password")
        if temperature > 25:
            smtp.send_message(content) # 寄送郵件
            print("Mailed!")
        elif temperature < 18:
            smtp.send_message(content1)
            print("Mailed!")
        else:
            print("Unmailed")
    except Exception as e:
        print("Error message: ", e)

