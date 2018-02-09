from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, hipsterGetResult, anime, getAnimeGrup
from telebot import types


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am Anime Bot.\n"
                  "You can get Hipster Ipsum Paragraph.\n"
                  "Example: \hipsteripsum N.\n"
                  "N is how many paragraph you want and it's integer but it's optional.\n"
                  "Value of N is from 1 until 99"
                  ))


@bot.message_handler(regexp=r'^/about$')
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'Anime Bot\n'
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


@bot.message_handler(regexp=r'^/hipsteripsum( )([-](\d)?|(\d)?)(\d)?\d')
def hipsterIpsumWithParam(message):
    app.logger.debug("'hipsteripsum' command detected")
    commandStr = message.text.split(' ')
    jumParagraph = commandStr[1]
    jumParagraphInvalid = int(jumParagraph)

    if jumParagraphInvalid <= 0:
        result = "Minimum value of N is 1"
    elif jumParagraphInvalid > 99:
        result = "Maximum value of N is 99"
    else:
        result = hipsterGetResult(jumParagraph)
        if len(result) > 4096:
            result = "Telegram cannot show more than 4096 char"

    bot.reply_to(message, result)


@bot.message_handler(regexp=r'^/hipsteripsum (\w)*')
def hipsterIpsumWordParam(message):
    app.logger.debug("'hipsteripsum' command detected")
    result = "Please insert parameter with integer not word"

    bot.reply_to(message, result)


@bot.message_handler(regexp=r'^/hipsteripsum')
def hipsterIpsumNoParam(message):
    app.logger.debug("'hipsteripsum' command detected")
    result = hipsterGetResult()

    bot.reply_to(message, result)


@bot.message_handler(regexp=r'^/is_airing .*')
def animeAir(message):
    if message.chat.type == "group":
        bot.reply_to(message, "Perintah ini hanya untuk Private Chat")
    else:
        app.logger.debug("'is_airing' command detected")
        animeName = message.text.split('/is_airing ')
        result = anime(animeName[1])
        pesan = ""
        if result == "Your Anime cannot be found":
            pesan = result
        else:
            pesan = result

        bot.reply_to(message, pesan)


@bot.message_handler(regexp=r'^/is_airing')
def noAnimeParam(message):
    chat_id = message.chat.id
    if message.chat.type == "group":
        bot.reply_to(message, "Perintah ini hanya untuk Private Chat")
    else:
        app.logger.debug("'is_airing' command detected")
        # result = "Please Insert Anime Name"
        # bot.reply_to(message, result)
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('a')
        itembtn2 = types.KeyboardButton('v')
        itembtn3 = types.KeyboardButton('d')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(regexp=r'^hari ini nonton apa\?')
def animeGroup(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "Input ini hanya untuk Grup Chat")
    else:
        result = getAnimeGrup()
        bot.reply_to(message, result)
