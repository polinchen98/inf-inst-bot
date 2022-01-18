import requests
from telebot import TeleBot, types
from credits import bot_token
from inst import parse


bot = TeleBot(bot_token)

instagram_url = 'https://www.instagram.com/'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет✌️. Напиши ник инстаграмм. ")
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Тык", url="https://github.com/polinchen98/inf-inst-bot")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Кликни на кнопку, чтобы посмотреть код:)", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    nickname = message.text
    headers = {
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        'accept-language': 'ru-RU,ru;q=0.9',
    }

    session = requests.session()
    response = session.get(instagram_url + nickname, headers=headers)

    try:
        followers, following, publications, average_comments, average_likes = parse(response.text)
        answer = f'• Подписчиков {followers}' + '\n' + f'• Подписок {following}' + \
                 '\n' + f'• Публикаций {publications}' + '\n' \
                 + f'• Среднее количество комментариев {average_comments}' + '\n' \
                 + f'• Среднее количество лайков {average_likes}'

        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, 'Не получилось:( \nПопробуйте позже')


bot.polling(none_stop=True)
