from unittest.mock import Mock

from csuibot.handlers import help, zodiac, shio, send_welcome, compute, invalidCompute


def test_send_welcome(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()

    send_welcome(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
       "Hi there, I am Binary Arithmetic Bot.\n"
       "Please insert a command with 2 binary operand. \n"
       "Example: /compute 0001*0101. \n"
       "You can do additon,substraction,multiplication,divison,and modulo"
    )
    assert args[1] == expected_text


def test_help(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mock_message = Mock()

    help(mock_message)

    args, _ = mocked_reply_to.call_args
    expected_text = (
        'Binary Arithmetic Bot\n\n'
        'Created by MFAUZANF'
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


def test_compute_tambah(mocker):
    result = '6'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.proses', return_value=result)
    mock_message = Mock(text='/compute 0010+0100')

    compute(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == result


def test_compute_kurang(mocker):
    result = '-2'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.proses', return_value=result)
    mock_message = Mock(text='/compute 0010-0100')

    compute(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == result


def test_compute_kali(mocker):
    result = '8'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.proses', return_value=result)
    mock_message = Mock(text='/compute 0010*0100')

    compute(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == result


def test_compute_bagi(mocker):
    result = '0.5'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.proses', return_value=result)
    mock_message = Mock(text='/compute 0010/0100')

    compute(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == result


def test_compute_mod(mocker):
    result = '2'
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.proses', return_value=result)
    mock_message = Mock(text='/compute 0010%0100')

    compute(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == result


def test_invalidCompute(mocker):
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.compute')
    mock_message = Mock(text='/compute')

    invalidCompute(mock_message)

    args, _ = mocked_reply_to.call_args
    result = "Your input invalid. Please insert operand or convert operand in binary"
    assert args[1] == result


def test_computeInvalidOperator(mocker):
    result = "Please insert operator '+', '-', '*', '/', '%'"
    mocked_reply_to = mocker.patch('csuibot.handlers.bot.reply_to')
    mocker.patch('csuibot.handlers.compute', return_value=result)
    mock_message = Mock(text='/compute 0010$0100')

    compute(mock_message)

    args, _ = mocked_reply_to.call_args
    assert args[1] == result
