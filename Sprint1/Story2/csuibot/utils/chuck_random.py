import urllib.request
import json


def chuck_random():
    try:
        response = urllib.request.urlopen('http://api.icndb.com/jokes/random')
    except OSError:
        raise OSError
    else:
        line = response.read().decode("utf-8")
        data = json.loads(line)

        return (data['value']['joke'])
