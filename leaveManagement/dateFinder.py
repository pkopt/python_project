from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re


def dateFinder(datestring):
    session = HTMLSession()

    url = "https://www.calendarlabs.com/holidays/india/2019"
    page_source = session.get(url, verify=False)

    soup = BeautifulSoup(page_source.text)

    subtitles = soup.findAll("span", {'class': "pc"})

    count = 1
    clean = re.compile('<.*?>')
    listofHoliday = []

    for i in subtitles:
        if count % 2 == 0:
            text = re.sub(clean, '', str(i))
            listofHoliday.append(text)

        count = count + 1
    if datestring in listofHoliday:
        return  True
    else:
        return False








