import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

# function for getting update
res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
cases = soup.find('div',{'class':'maincounter-number'}).get_text().strip()

# function for notification
def notify(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

while True:
    notify('Total np. of cases: ',cases)
    time.sleep(30)