import json
import urllib.request
from urllib.parse import quote


def look_article(query=''):
    query = quote(query.lower())
    link = ('https://en.wikipedia.org/w/api.php?'
            'format=json&action=query&prop=extracts&exchars=4000'
            '&exintro=&explaintext=&redirects=1&titles='
            + query)
    with urllib.request.urlopen(link) as response:
        json_files = response.read()
        encode_json = response.info().get_content_charset('utf-8')
        results = json.loads(json_files.decode(encode_json))
    try:
        if('query' not in results.keys()):
            return "Query is empty!"
        elif('-1' in results["query"]["pages"].keys()):
            return "Page not found!"
        else:
            id = list(results["query"]["pages"])
            return (results["query"]["pages"][id[0]]["extract"]
                    + "\nhttps://en.wikipedia.org/wiki/" + query)
    except Exception:
        return "Unexpected Error"


def search_article(query):
    try:
        urllib.request.urlopen('https://en.wikipedia.org/', timeout=100)
    except urllib.error.URLError:
        return "Masalah koneksi"

    return look_article(query)
