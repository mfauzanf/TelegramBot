import random
import requests


def load_memes():
    try:
        response = requests.get("https://api.imgflip.com/get_memes")
    except Exception:
        return ('Problem when connecting to API')
    results = response.json()
    try:
        return results['data']['memes']
    except Exception:
        return "Error retrieving memes"


def search_memes(keywords, memes):
    # Search for memes based on query given
    # Ridulously simple meme finding
    for i in memes:
        if (keywords.lower() in i['name'].lower() or i['name'].lower() in keywords.lower()):
            return i['id']
    return '-1'


def random_memes(memes):
    # Pick random memes
    pos = random.randint(0, 99)
    return memes[pos]['id']


def get_meme(top='', bottom=''):
    # Load Memes first
    memes = load_memes()

    if(type(memes) is not list):
        # Memes is now an error message
        return memes

    memeId = search_memes(top+''+bottom, memes)
    if(memeId == '-1'):
        memeId = random_memes(memes)

    if(top is not '' or bottom is not ''):
        memeData = {
            'template_id': memeId,
            'username': 'victim_crasher',
            # ridiculously unsafe!
            'password': 'buatbot',
            'text0': top,
            'text1': bottom
        }
    else:
        for i in memes:
            if memeId == i['id']:
                return i['url']

    try:
        r = requests.post("https://api.imgflip.com/caption_image", data=memeData)
        r = r.json()
    except Exception:
        return 'Problem when creating memes'

    if(r['success'] is False):
        return r['error_message']
    return r['data']['url']
