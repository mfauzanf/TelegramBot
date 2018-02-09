from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, hipsterGetResult, getNews


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am Relevant News Bot.\n"
                  "You can get 5 news\n"
                  "Example: /news [topic].\n"
                  "topic is something you want to get the info"
                  ))


@bot.message_handler(regexp=r'^/about$')
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'Relevant News Bot.\n'
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


@bot.message_handler(regexp=r'^/news .*')
def news(message):
    app.logger.debug("'news' command detected")
    commandStr = message.text.split('/news')
    topic = commandStr[1]
    result = getNews(topic)

    bot.reply_to(message, result)


@bot.message_handler(regexp=r'^/news')
def newsNoTopic(message):
    result = "Please Insert the topic"

    bot.reply_to(message, result)
