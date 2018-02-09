import requests
from html.parser import HTMLParser


class SceleParser(HTMLParser):
    def __init__(self, urls):
        HTMLParser.__init__(self)
        self.handle = "none"
        self.list_news = []
        self.current = {}
        self.urls = urls
        self.index_urls = 0

    def handle_starttag(self, tag, attrs):
        if tag == "a" and self.handle == "author_div":
            self.handle = "author_a"
        elif self.handle != "posting":
            self.handle = ""
        if tag == "div":
            self.check_div(attrs)

    def check_div(self, attrs):
        for (name, value) in attrs:
            if name == "class":
                if value == "forumpost clearfix firstpost starter":
                    self.current = {}
                    self.current["url"] = self.urls[self.index_urls]
                    self.index_urls += 1
                if value == "subject":
                    self.handle = "new_subject"
                if value == "author":
                    self.handle = "author_div"
                if value == "posting fullpost":
                    self.current["summary"] = ""
                    self.handle = "posting"
                if value == "posting shortenedpost":
                    self.current["summary"] = ""
                    self.handle = "posting"

    def handle_endtag(self, tag):
        if self.handle == "posting" and tag == "div":
            self.handle = ""
            self.list_news.append(self.current)

    def handle_data(self, data):
        if self.handle == "new_subject":
            self.current["judul"] = data
        if self.handle == "author_a":
            if "penulis" in self.current:
                self.current["tanggal"] = data[3:]
            else:
                self.current["penulis"] = data
        if self.handle == "posting":
            self.current["summary"] += data + "\n"


class ScelePengumumanAkademisParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.list_url = []
        self.accepting_url = False
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if tag == "a" and self.accepting_url:
            for (name, value) in attrs:
                if name == "href":
                    self.list_url.append(value)
                    self.count += 1
                    self.accepting_url = False
        if tag == "td":
            for (name, value) in attrs:
                if name == "class" and value == "topic starter" and self.count < 5:
                    self.accepting_url = True


def get_scele_time():
    try:
        response = requests.get("https://scele.cs.ui.ac.id/", timeout=10)
    except requests.exceptions.RequestException:
        return "request to scele failed"
    datetime = response.headers["Date"].split(" ")
    day = datetime[0][:-1]
    time = datetime[4].split(":")
    hour = (int(time[0]) + 7) % 24
    return day + " " + str(hour) + ":" + time[1] + ":" + time[2]


def get_scele_notice():
    try:
        resp = requests.get("https://scele.cs.ui.ac.id/mod/forum/view.php?id=1")
    except requests.exceptions.RequestException:
        return "gagal"
    parser = ScelePengumumanAkademisParser()
    parser.feed(resp.text)

    try:
        resp = requests.get("https://scele.cs.ui.ac.id")
    except requests.exceptions.RequestException:
        return "gagal"
    parser = SceleParser(parser.list_url)
    parser.feed(resp.text)
    return parser.list_news
