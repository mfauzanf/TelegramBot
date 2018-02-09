
import requests


class bingNews():
    def __init__(self, args):
        self.bingNewsAPI = "https://api.cognitive.microsoft.com/bing/v5.0/news/search?q="
        self.query = args
        self.key = {'Ocp-Apim-Subscription-Key': 'be33fca3ab27480eac00475c986d1217'}

    def getFiveNews(self):
        r = requests.get(self.bingNewsAPI+self.query, headers=self.key)
        self.result = r.json()
        count = 0
        abc = ''

        for entry in self.result.get('value'):
            abc += entry['name'] + '\n' + '\n'
            abc += entry['description'] + '\n' + entry['url'] + '\n'
            abc += '\n'
            count += 1
            if count == 5:
                break

        return abc
