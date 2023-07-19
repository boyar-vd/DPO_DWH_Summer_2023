from datetime import datetime
with open('/Users/vladislavboyar/Desktop/HSE/HSE_DPO_DWH/log.txt', 'a') as f:
    f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' Hello, I am test crontab task! \n')
    f.close()
