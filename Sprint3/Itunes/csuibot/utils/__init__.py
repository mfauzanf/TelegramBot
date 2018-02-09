from csuibot.utils import zodiac as z, hitungBinary as hb, audioPreview as ap
from random import randint


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


def convertOperand(binary):
    return int(str(binary), 2)


def proses(bin1, bin2, jenisOperator):
    decimal1 = convertOperand(bin1)
    decimal2 = convertOperand(bin2)
    hitung = hb.hitungBinary(decimal1, decimal2)
    hasil = ''

    if jenisOperator == "tambah":
        hasil = hitung.tambah()
    elif jenisOperator == "kurang":
        hasil = hitung.kurang()
    elif jenisOperator == "kali":
        hasil = hitung.kali()
    elif jenisOperator == "bagi":
        hasil = hitung.bagi()
    elif jenisOperator == "mod":
        hasil = hitung.mod()

    return str(hasil)


def findArtistAudio(artistName):
    audio = ap.audioPreview(artistName)
    result = ''
    trackPreviewList = audio.getPreviewList()
    if (trackPreviewList is False):
        result = False
    else:
        index = randint(0, len(trackPreviewList))
        result = trackPreviewList[index]

    return result
