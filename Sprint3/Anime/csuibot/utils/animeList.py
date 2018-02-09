import requests
import xml.etree.ElementTree as ET


class animeList():
    def __init__(self, args):
        self.myAnimeAPI = "https://myanimelist.net/api/anime/search.xml?q="
        self.namaAnime = args
        self.user = "KyojinYeager"
        self.password = "@ttacK$#@7890"

    def getData(self):
        r = requests.get(self.myAnimeAPI+self.namaAnime, auth=(self.user, self.password))
        root = r.text
        return root

    def proses(self, data):
        c = ET.fromstring(data)
        a = len(c.findall("entry"))
        count = 0
        str = ''

        while count != a:
            if c[count][7].text == "Finished Airing":
                str += c[count][1].text + " has finished airing at " + c[count][9].text
                str += "\n"
                str += "\n"
            elif c[count][7].text == "Currently Airing":
                str += c[count][1].text + " is airing from " + c[count][8].text + " until "
                str += c[count][9].text + "\n"
                str += "\n"
            elif c[count][7].text == "Not yet aired":
                str += c[count][1].text + " will air starting at " + c[count][8].text
                str += "\n"
                str += "\n"
            count += 1

        return str
