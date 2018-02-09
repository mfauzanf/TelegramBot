import requests
import xml.etree.ElementTree as ET


class tropicalProses():

    def __init__(self):
        self.rssFEED = "http://www.billboard.com/rss/charts/tropical-songs"
        r = requests.get(self.rssFEED)
        self.root = ET.fromstring(r.text)
        self.dataXML = self.root
        self.listSong = []
        self.listRank = []
        self.listArtist = []
        self.detailData = []

    def getArtist(self):
        a = 4
        while a < 24:
            artist = self.dataXML[0][a][2].text
            self.listArtist.append(artist)
            a += 1

    def getSong(self):
        a = 4
        while a < 24:
            song = self.dataXML[0][a][3].text
            self.listSong.append(song)
            a += 1

    def getRank(self):
        a = 4
        while a < 24:
            rank = self.dataXML[0][a][4].text
            self.listRank.append(rank)
            a += 1

    def checkArtist(self, param):
            if(param in self.listArtist):
                return True
            else:
                return False

    def getArtistDetailData(self, param):
        index = self.listArtist.index(param)
        artist = self.listArtist[index]
        song = self.listSong[index]
        rank = self.listRank[index]
        self.detailData.append(artist)
        self.detailData.append(song)
        self.detailData.append(rank)
        return self.detailData
