from unittest.mock import Mock
from csuibot.handlers import help, zodiac, shio, send_welcome
from csuibot.handlers import hipsterIpsumWithParam, hipsterIpsumNoParam, hipsterIpsumWordParam
from csuibot.handlers import news, newsNoTopic


def test_send_welcome(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()

    send_welcome(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
       "Hi there, I am Relevant News Bot.\n"
       "You can get 5 news\n"
       "Example: /news [topic].\n"
       "topic is something you want to get the info"
    )
    assert args[1] == expected_text


def test_help(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()

    help(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
        'Relevant News Bot.\n'
        'Created by @MFAUZANF'
    )
    assert args[1] == expected_text


def test_zodiac(mocker):
    fake_zodiac = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_zodiac', return_value=fake_zodiac)
    mock_message = Mock(text='/zodiac 2015-05-05')

    zodiac(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_zodiac


def test_zodiac_invalid_month_or_day(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_zodiac', side_effect=ValueError)
    mock_message = Mock(text='/zodiac 2015-25-05')

    zodiac(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == 'Month or day is invalid'


def test_shio(mocker):
    fake_shio = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_chinese_zodiac', return_value=fake_shio)
    mock_message = Mock(text='/shio 2015-05-05')

    shio(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_shio


def test_shio_invalid_year(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.lookup_chinese_zodiac', side_effect=ValueError)
    mock_message = Mock(text='/shio 1134-05-05')

    shio(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == 'Year is invalid'


def test_hipsterIpsumWithParameter(mocker):
    fake_text = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.hipsterGetResult', return_value=fake_text)
    mock_message = Mock(text='/hipsteripsum 1')

    hipsterIpsumWithParam(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_text


def test_hipsterIpsumNoParameter(mocker):
    fake_text = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.hipsterGetResult', return_value=fake_text)
    mock_message = Mock(text='/hipsteripsum')

    hipsterIpsumNoParam(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_text


def test_hipsterIpsumWordParameter(mocker):
    fake_param = "Please insert parameter with integer not word"
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.hipsterGetResult', return_value=fake_param)
    mock_message = Mock(text='/hipsteripsum coba')

    hipsterIpsumWordParam(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_param


def testNews(mocker):
    fake_text = 'foo bar'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.getNews', return_value=fake_text)
    mock_message = Mock(text='/news Linkin Park')

    news(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == fake_text


def testNoTopic(mocker):
    result = 'Please Insert the topic'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers', return_value=result)
    mock_message = Mock(text='/news')

    newsNoTopic(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == result
