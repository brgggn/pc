#_________________________
import telebot
from telebot import types

import os

#поиск файлов в дириктории
import glob

#платформа сервера
import platform

#для копирования
import pyperclip

#для вставки
from pymouse import *
from pykeyboard import *

mouse = PyMouse ()
keyboard = PyKeyboard ()

#для скриншотов
import pyautogui



#_________________________
def book(com):
    comand = {
        'about': 'о проекте',
        'copy': 'копировать',
        'insert': 'вставить',
        'screenshot': 'скриншот',
        'win_r': 'win_r',
        'enter': 'enter',

        'about1': 'Программа создана пользователем telegram - @ mx6786\n'
                  'Принимает: голосовые, видео, изоброжения, документы, текст, видеосообщения, ссылки и отправляет на по нужному пути',
        'insert1': 'вставиk;)',

        'nyza': 'Низя',


        'txt': 'Текст;)',
        'document': 'Документ;)',
        'photo': 'Изображение;)',
        'video': 'Видео;)',
        'audio': 'Аудио;)',
        'voice': 'Голосовое;)',
        'video_note': 'Видеосообщение;)',
        'sticker': 'Стикер;)',

    }
    return comand.get(com)

def api():
    return open('api.txt').read().split('\n')

adm, bot, put, chan = api()[0], telebot.TeleBot(api()[1]), api()[2] + '/', api()[3]

#________________________
try:
    bot.send_message(chan, f'bot working\n@BotPersonalComputerBot')
    bot.send_message(adm, f'{platform.system()} {platform.release()}, {os.getlogin()} - /start')

except: pass


#________________________
try: os.mkdir("dok")
except: pass
#________________________
try:
    def a_start(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup.row(types.KeyboardButton('play'), types.KeyboardButton(book('copy')), types.KeyboardButton(book('insert')))
            markup.row(types.KeyboardButton(book('screenshot')), types.KeyboardButton(book('win_r')), types.KeyboardButton(book('enter')))
            markup.row(types.KeyboardButton(book('about')))

            bot.send_message(message.chat.id, 'проект - @mx6786', reply_markup=markup)

    def a_about(message):
        bot.send_message(adm, book('about1'))

    def a_play(message):
        try:
            name_file = glob.glob('dok\*')

            file = 'file:'
            for i in range(len(name_file)):
                file += f'\n{i+1}) {name_file[i][4:]}'

            bot.send_message(adm, file)

            for i in range(len(name_file)):
                bot.send_document(adm, open(name_file[i], 'rb'))

                (open(name_file[i])).close()
                os.remove(name_file[i])
            (open('dok')).close()
        except:
            pass


    def a_copy(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            bot.send_message(adm, pyperclip.paste())

    def a_insert(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            keyboard.type_string(pyperclip.paste())
            bot.reply_to(message, f"{book('insert1')} - {pyperclip.paste()}")

    def a_screenshot(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            img_name = 'screenshot.png'
            img = pyautogui.screenshot()
            img.save(img_name)

            im = open(img_name, 'rb')
            bot.send_document(message.chat.id, im)
            im.close()
            os.remove(img_name)

    def a_alt_tab(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            keyboard.press_key(keyboard.alt_key)
            keyboard.tap_key(keyboard.tab_key)
            keyboard.release_key(keyboard.alt_key)

    def a_win_r(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            keyboard.press_key(keyboard.windows_l_key)
            keyboard.tap_key('r')
            keyboard.release_key(keyboard.windows_l_key)

    def a_enter(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            keyboard.tap_key(keyboard.enter_key)

    @bot.message_handler(commands=['Start', 'start'])
    def c_start(message): a_start(message)

    @bot.message_handler(commands=['Play', 'play'])
    def c_start(message): a_play(message)

    @bot.message_handler(commands=['Copy', 'copy'])
    def c_start(message): a_copy(message)

    @bot.message_handler(commands=['Insert', 'insert'])
    def c_start(message): a_insert(message)

    @bot.message_handler(commands=['Screenshot', 'screenshot'])
    def c_start(message): a_screenshot(message)

    @bot.message_handler(commands=['Win_r', 'win_r'])
    def c_start(message): a_win_r(message)

    @bot.message_handler(commands=['Alt_tab', 'alt_tab'])
    def c_start(message): a_alt_tab(message)

    @bot.message_handler(commands=['Enter', 'enter'])
    def c_start(message): a_enter(message)

    @bot.message_handler(content_types=['text'])
    def textmessages(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            if message.text.lower() == book('about'):
                a_about(message)

            elif message.text.lower() == 'play':
                a_play(message)

            elif message.text.lower() == book('copy'):
                a_copy(message)

            elif message.text.lower() == book('insert'):
                a_insert(message)

            elif message.text.lower() == book('screenshot'):
                a_screenshot(message)

            elif message.text.lower() == book('win_r'):
                a_win_r(message)

            elif message.text.lower() == book('enter'):
                a_enter(message)

            else:
                '''
                my_file = open(put + 'text.txt', 'w')
                text_for_file = message.text
                my_file.write(text_for_file)
                my_file.close()
                bot.reply_to(message, book("txt"))'''
                pyperclip.copy(message.text)
                spam = pyperclip.paste()
                bot.reply_to(message, book("txt"))
    #________________________
    # документ
    @bot.message_handler(content_types=['document'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            try:
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + message.document.file_name
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, book("document"))
            except Exception as e:
                bot.reply_to(message, e)

    # фото
    @bot.message_handler(content_types=['photo'])
    def handle_docs_photo(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            try:
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[7:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, book("photo"))
            except Exception as e:
                bot.reply_to(message, e)

    # видео
    @bot.message_handler(content_types=['video'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            try:
                file_info = bot.get_file(message.video.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[7:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, book("video"))
            except Exception as e:
                bot.reply_to(message, e)
    #________________________
    # аудио
    @bot.message_handler(content_types=['audio'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            try:
                file_info = bot.get_file(message.audio.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[6:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, book("audio"))
            except Exception as e:
                bot.reply_to(message, e)
    #________________________
    # голосовуха
    @bot.message_handler(content_types=['voice'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            try:
                file_info = bot.get_file(message.voice.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[6:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, book("voice"))
            except Exception as e:
                bot.reply_to(message, e)

    #________________________
    # видеосообщение
    @bot.message_handler(content_types=['video_note'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            try:
                file_info = bot.get_file(message.video_note.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[12:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, book("video_note"))
            except Exception as e:
                bot.reply_to(message, e)

        # Стикер
    @bot.message_handler(content_types=['sticker'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, book('nyza'))
        else:
            try:
                file_info = bot.get_file(message.sticker.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + (file_info.file_path[8:].split('.'))[0] + '.png'
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, book("sticker"))
            except Exception as e:
                bot.reply_to(message, e)



except Exception as e: bot.send_message(adm, e)


# ссылка
#________________________
bot.polling(none_stop=True)
