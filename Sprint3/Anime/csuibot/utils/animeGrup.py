from bs4 import BeautifulSoup
import datetime
import requests
import pytz


class animeGrup():
    def __init__(self):
        self.web = "https://www.livechart.me/spring-2017/tv"

    def getData(self):
        page = requests.get(self.web)
        japanDate = datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo'))
        soup = BeautifulSoup(page.content, 'html.parser')
        z = soup.find_all('time')
        x = soup.find_all('div', class_='episode-countdown')
        c = soup.find_all('h3', class_='main-title')
        tglAnime = []
        judulAnime = []
        epsAnime = []
        day = str(japanDate.day)
        string = ''

        for jam in z:
            text2 = jam.get_text().split(" ")
            tglAnime.append(text2[1])

        for judul in c:
            judulAnime.append(judul.get_text())

        for eps in x:
            text4 = eps.get_text().split(": ")
            epsAnime.append(text4[0])

        count = 0
        while count != len(tglAnime):
            if tglAnime[count] == day:
                ep = epsAnime[count].split("EP")
                string += judulAnime[count] + " " + ep[1]
                string += "\n"
            count += 1

        return string
