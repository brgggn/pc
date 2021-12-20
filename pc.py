#________________________
import os
import platform
import glob
import telebot
from telebot import types
#________________________
def startpac(com):
    comand = {
        'nyza': 'Низя',
    }
    return comand.get(com)

def rkm(com):
    comand = {
        'about': 'о проекте',
    }
    return comand.get(com)

def api():
    f = open('api.txt')
    r = f.read()
    nrs = r.split(';')
    return nrs

adm = api()[0]
bot = telebot.TeleBot(api()[1])
put = api()[2]
#________________________
try: bot.send_message(adm, f'{platform.system()} {platform.release()}, {os.getlogin()} - /start')
except: pass
#________________________
try: os.mkdir("dok")
except: pass
#________________________
try:
    def a_start(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, startpac('nyza'))
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup.row(types.KeyboardButton('play'), types.KeyboardButton(rkm('about')))

            bot.send_message(message.chat.id, 'проект - @mx6786', reply_markup=markup)

    def a_about(message):
        bot.send_message(adm, 'about...')

    def a_play(message):
        try:
            name_file = glob.glob('dok\*')
            for i in range(len(name_file)):
                bot.send_message(adm, f'file - {name_file[i]}')
                bot.send_document(adm, open(name_file[i], 'rb'))

                (open(name_file[i])).close()
                os.remove(name_file[i])
        except:
            pass

    @bot.message_handler(commands=['Start', 'start'])
    def c_start(message): a_start(message)

    @bot.message_handler(commands=['Play', 'play'])
    def c_start(message): a_play(message)

    @bot.message_handler(content_types=['text'])
    def textmessages(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, startpac('nyza'))
        else:
            if message.text.lower() == rkm('about'):
                a_about(message)

            elif message.text.lower() == 'play':
                a_play(message)

            else:
                my_file = open(put + 'text.txt', 'w')
                text_for_file = message.text
                my_file.write(text_for_file)
                my_file.close()
                bot.reply_to(message, "txt;)")
    #________________________
    # документ
    @bot.message_handler(content_types=['document'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, startpac('nyza'))
        else:
            try:
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + message.document.file_name
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "document;)")
            except Exception as e:
                bot.reply_to(message, e)

    # фото
    @bot.message_handler(content_types=['photo'])
    def handle_docs_photo(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, startpac('nyza'))
        else:
            try:
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[7:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "photo;)")
            except Exception as e:
                bot.reply_to(message, e)

    # видео
    @bot.message_handler(content_types=['video'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, startpac('nyza'))
        else:
            try:
                file_info = bot.get_file(message.video.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[7:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "video;)")
            except Exception as e:
                bot.reply_to(message, e)
    #________________________
    # аудио
    @bot.message_handler(content_types=['audio'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, startpac('nyza'))
        else:
            try:
                file_info = bot.get_file(message.audio.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[6:]
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "audio;)")
            except Exception as e:
                bot.reply_to(message, e)
    #________________________
    # голосовуха
    @bot.message_handler(content_types=['voice'])
    def handle_docs_document(message):
        if str(message.chat.id) != adm:
            bot.send_message(message.chat.id, startpac('nyza'))
        else:
            try:
                file_info = bot.get_file(message.voice.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = put + file_info.file_path[6:]
                print(src)
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "voice;)")
            except Exception as e:
                bot.reply_to(message, e)

except Exception as e: bot.send_message(adm, e)
# ссылка
# текст
#________________________
bot.polling(none_stop=True)
