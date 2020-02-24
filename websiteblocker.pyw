import time
from datetime import datetime as dt
import pandas as pd

data = pd.read_csv("websitelist.txt")

host_temp = "D:\\Users\\Sunny\\Code\\Python\\WebsiteBlocker\\hosts"
# host_name = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
website_list = list(data['WEBSITE'])


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        with open(host_temp, "r+") as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
