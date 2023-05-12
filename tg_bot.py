# Подключаем модуль для Телеграма
import telebot
from bs4 import BeautifulSoup
import requests
# Указываем токен
bot = telebot.TeleBot('6298309827:AAFKFkaDBHF2eIzmvwz0M_q80qCDbn6TPXI')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
def get_text(url1):
    rs = requests.get(url1)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url1 = 'https://fakty.ua/ru/horoscope/1'
def get_text(url2):
    rs = requests.get(url2)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url2 = 'https://fakty.ua/ru/horoscope/2'
def get_text(url3):
    rs = requests.get(url3)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url3 = 'https://fakty.ua/ru/horoscope/3'
def get_text(url4):
    rs = requests.get(url4)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url4 = 'https://fakty.ua/ru/horoscope/4'
def get_text(url5):
    rs = requests.get(url5)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url5 = 'https://fakty.ua/ru/horoscope/5'
def get_text(url6):
    rs = requests.get(url6)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url6 = 'https://fakty.ua/ru/horoscope/6'
def get_text(url7):
    rs = requests.get(url7)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url7 = 'https://fakty.ua/ru/horoscope/7'
def get_text(url8):
    rs = requests.get(url8)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url8 = 'https://fakty.ua/ru/horoscope/8'
def get_text(url9):
    rs = requests.get(url9)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url9 = 'https://fakty.ua/ru/horoscope/9'
def get_text(url10):
    rs = requests.get(url10)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url10 = 'https://fakty.ua/ru/horoscope/10'
def get_text(url11):
    rs = requests.get(url11)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url11 = 'https://fakty.ua/ru/horoscope/11'
def get_text(url12):
    rs = requests.get(url12)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('p')
    return article.text

url12 = 'https://fakty.ua/ru/horoscope/12'
# Импортируем типы из модуля, чтобы создавать кнопки

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет" or "привет"  or "привіт":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='oven')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='telec')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='bliznecy')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='rak')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='lev')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='deva')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='vesy')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='scorpion')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='strelec')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='kozerog')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='vodoley')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='ryby')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == 'oven':
        # Формируем гороскоп
        mgs1 = 'Гороскоп для Овнов на сегодня: '
        text1 = get_text(url1)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs1)
        bot.send_message(call.message.chat.id, text1)
    if call.data == 'telec':
        # Формируем гороскоп
        mgs2 = 'Гороскоп для Тельцов на сегодня: '
        text2 = get_text(url2)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs2)
        bot.send_message(call.message.chat.id, text2)
    if call.data == 'bliznecy':
        # Формируем гороскоп
        mgs3 = 'Гороскоп для Близнецов на сегодня: '
        text3 = get_text(url3)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs3)
        bot.send_message(call.message.chat.id, text3)
    if call.data == 'rak':
        # Формируем гороскоп
        mgs4 = 'Гороскоп для Раков на сегодня: '
        text4 = get_text(url4)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs4)
        bot.send_message(call.message.chat.id, text4)
    if call.data == 'lev':
        # Формируем гороскоп
        mgs5 = 'Гороскоп для Львов на сегодня: '
        text5 = get_text(url5)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs5)
        bot.send_message(call.message.chat.id, text5)
    if call.data == 'deva':
        # Формируем гороскоп
        mgs6 = 'Гороскоп для Дев на сегодня: '
        text6 = get_text(url6)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs6)
        bot.send_message(call.message.chat.id, text6)
    if call.data == 'vesy':
        # Формируем гороскоп
        mgs7 = 'Гороскоп для Весов на сегодня: '
        text7 = get_text(url7)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs7)
        bot.send_message(call.message.chat.id, text7)
    if call.data == 'scorpion':
        # Формируем гороскоп
        mgs8 = 'Гороскоп для Скорпионов на сегодня: '
        text8 = get_text(url8)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs8)
        bot.send_message(call.message.chat.id, text8)
    if call.data == 'strelec':
        # Формируем гороскоп
        mgs9 = 'Гороскоп для Стрельцов на сегодня: '
        text9 = get_text(url9)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs9)
        bot.send_message(call.message.chat.id, text9)
    if call.data == 'kozerog':
        # Формируем гороскоп
        mgs10 = 'Гороскоп для Козерогов на сегодня: '
        text10 = get_text(url10)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs10)
        bot.send_message(call.message.chat.id, text10)
    if call.data == 'vodoley':
        # Формируем гороскоп
        mgs11 = 'Гороскоп для Водолеев на сегодня: '
        text11 = get_text(url11)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs11)
        bot.send_message(call.message.chat.id, text11)
    if call.data == 'ryby':
        # Формируем гороскоп
        mgs12 = 'Гороскоп для Рыб на сегодня: '
        text12 = get_text(url12)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, mgs12)
        bot.send_message(call.message.chat.id, text12)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
