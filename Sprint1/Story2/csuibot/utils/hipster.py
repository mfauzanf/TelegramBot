import requests


class hipsterProses():
    def __init__(self, args):
        self.hipsterAPI = "http://hipsterjesus.com/api"
        self.data = {'paras': args}

    def getData(self):
        self.data['html'] = "false"
        r = requests.get(self.hipsterAPI, params=self.data)
        self.result = r.json()
        self.paragraph = self.result['text']

        return self.paragraph
