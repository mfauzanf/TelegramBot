from csuibot.utils import zodiac as z, hipster as h
from csuibot.utils import animeList as al, animeGrup as ag


def lookup_zodiac(month, day):
    zodiacs = [
        z.Aries(),
        z.Taurus(),
        z.Gemini(),
        z.Cancer(),
        z.Leo(),
        z.Virgo(),
        z.Libra(),
        z.Scorpio(),
        z.Sagittarius(),
        z.Capricorn(),
        z.Aquarius(),
        z.Pisces()
    ]

    for zodiac in zodiacs:
        if zodiac.date_includes(month, day):
            return zodiac.name
    else:
        return 'Unknown zodiac'


def lookup_chinese_zodiac(year):
    num_zodiacs = 12
    zodiacs = {
        0: 'rat',
        1: 'buffalo',
        2: 'tiger',
        3: 'rabbit',
        4: 'dragon',
        5: 'snake',
        6: 'horse',
        7: 'goat',
        8: 'monkey'
    }
    ix = (year - 4) % num_zodiacs

    try:
        return zodiacs[ix]
    except KeyError:
        return 'Unknown zodiac'


def hipsterGetResult(args=1):
    hipsterResult = h.hipsterProses(args)

    return hipsterResult.getData()


def anime(animeName):
    animeList = al.animeList(animeName)
    data = animeList.getData()
    result = ""

    if data == "":
        result = "Your Anime cannot be found"
    else:
        result = animeList.proses(data)

    return result


def getAnimeGrup():
    grupAnim = ag.animeGrup()
    result = grupAnim.getData()
    pesan = ''

    if result == "":
        pesan = "There's no anime today"
    else:
        pesan = result

    return pesan
