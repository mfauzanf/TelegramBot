import requests


class audioPreview():
    def __init__(self, args):
        self.itunesAPI1 = "https://itunes.apple.com/search?term="
        self.artist = args
        self.itunesAPI2 = "&entity=song&limit=20"

    def getPreviewList(self):
        r = requests.get(self.itunesAPI1+self.artist+self.itunesAPI2)
        self.result = r.json()
        hasil = ''
        trackList = []
        if(len(self.result.get('results')) == 0):
            hasil = False
        else:
            for entry in self.result.get('results'):
                trackList.append(entry['previewUrl'])

            hasil = trackList

        return hasil
