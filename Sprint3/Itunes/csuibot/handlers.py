from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, proses, findArtistAudio


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am Itunes Preview Audio Bot.\n"
                  "Please insert a command with artist Name.\n"
                  "Example: /itunes_preview Linkin Park."
                  ))


@bot.message_handler(regexp=r'^/about$')
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'Itunes Preview Audio Bot\n'
        'Created by @MFAUZANF'
    )
    bot.reply_to(message, about_text)


@bot.message_handler(regexp=r'^/zodiac \d{4}\-\d{2}\-\d{2}$')
def zodiac(message):
    app.logger.debug("'zodiac' command detected")
    _, date_str = message.text.split(' ')
    _, month, day = parse_date(date_str)
    app.logger.debug('month = {}, day = {}'.format(month, day))

    try:
        zodiac = lookup_zodiac(month, day)
    except ValueError:
        bot.reply_to(message, 'Month or day is invalid')
    else:
        bot.reply_to(message, zodiac)


@bot.message_handler(regexp=r'^/shio \d{4}\-\d{2}\-\d{2}$')
def shio(message):
    app.logger.debug("'shio' command detected")
    _, date_str = message.text.split(' ')
    year, _, _ = parse_date(date_str)
    app.logger.debug('year = {}'.format(year))

    try:
        zodiac = lookup_chinese_zodiac(year)
    except ValueError:
        bot.reply_to(message, 'Year is invalid')
    else:
        bot.reply_to(message, zodiac)


def parse_date(text):
    return tuple(map(int, text.split('-')))


# Handler for all string that started with "/compute ..."
@bot.message_handler(regexp=r'^/compute [01]*[\+\*\/\%\-\$\w][01]*$')
def compute(message):
    app.logger.debug("'compute' command detected")
    _, commandStr = message.text.split(' ')
    hasil = ''
    if '+' in commandStr:
        a, b = tuple(commandStr.split('+'))
        hasil = proses(a, b, "tambah")
    elif '-' in commandStr:
        a, b = tuple(commandStr.split('-'))
        hasil = proses(a, b, "kurang")
    elif '*' in commandStr:
        a, b = tuple(commandStr.split('*'))
        hasil = proses(a, b, "kali")
    elif '/' in commandStr:
        a, b = tuple(commandStr.split('/'))
        hasil = proses(a, b, "bagi")
    elif '%' in commandStr:
        a, b = tuple(commandStr.split('%'))
        hasil = proses(a, b, "mod")
    else:
        hasil = "Please insert operator '+', '-', '*', '/', '%'"

    bot.reply_to(message, hasil)


@bot.message_handler(regexp=r'^/compute')
def invalidCompute(message):
    result = "Your input invalid. Please insert operand or convert operand in binary"
    bot.reply_to(message, result)


@bot.message_handler(regexp=r'^/itunes_preview [\s\S]+$')
def iTunesArtist(message):
    app.logger.debug("'itunes_preview' command detected")
    b = message.text.split("/itunes_preview ")
    artistName = b[1]
    logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/"
    logo += "Download_on_iTunes.svg/252px-Download_on_iTunes.svg.png"
    result = findArtistAudio(artistName)
    if result is False:
        bot.reply_to(message, "Artist Not Found")
    else:
        bot.reply_to(message, logo)
        bot.send_audio(message.chat.id, result)


@bot.message_handler(regexp=r'^/itunes_preview')
def noArtistName(message):
    result = "Please Insert Artist Name"
    bot.reply_to(message, result)
