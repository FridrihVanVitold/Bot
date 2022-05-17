import telebot
from telebot import types

# import config

bot = telebot.TeleBot("5368671679:AAEP2l5QK_gDX8Hqi4IjA1cfVqG13ve3N4I")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Топ')
    btn2 = types.KeyboardButton('Обязанности')
    btn3 = types.KeyboardButton('Каталог')
    btn4 = types.KeyboardButton('Маршрут')
    btn5 = types.KeyboardButton('Чаты')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    send_message = f'<b>Здраствуйте,{message.from_user.first_name} {message.from_user.last_name}.</b>\n Этот бот предоставляет актуальную рабочую информацию для наших сотрудников\nВоспользуйтесь меню '
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_mess(message):
    message.text = message.text.strip().lower()
    if message.text == 'топ':
        top = open('top20.jpg', 'rb')
        bot.send_photo(message.chat.id, top)
    elif message.text == 'обязанности':
        res1 = open('responsibility1.jpg', 'rb')
        res2 = open('responsibility2.jpg', 'rb')
        bot.send_message(message.chat.id, "Ваши обязанности")
        bot.send_photo(message.chat.id, res1)
        bot.send_photo(message.chat.id, res2)
    elif message.text == 'маршрут':
        rout = open('rout_may.xls', 'rb')
        bot.send_message(message.chat.id, "Маршруты мерчендайзеров на май месяц")
        bot.send_document(message.chat.id, rout)
    elif message.text == 'каталог':
        cat = open('Katalog_2020_2.pdf', 'rb')
        bot.send_message(message.chat.id, "Каталог нашей продукции")
        bot.send_document(message.chat.id, cat)
    elif message.text == 'чаты':
        chats = 'Рабочие чаты:\nПока нет ссылок на чаты, держите рофляну https://t.me/dvachannel'
        bot.send_message(message.chat.id, chats)
    else:
        bot.send_message(message.chat.id, 'Воспользуйтесь меню')






bot.polling(none_stop=True)

# @bot.message_handler(commands=['top'])
# def top(photo):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Top20"))
#     photo = open('top20.jpg', 'rb')
#     bot.send_photo(chat_id, , reply_markup=markup)
#
# @bot.message_handler(commands=['web'])
# def web(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True,)
#     website = types.KeyboardButton('Website')
#     start = types.KeyboardButton('Start')
#
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "spisok topov", reply_markup=markup)
