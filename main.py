import os
import time

import telebot
import key
import text
import func


bot = telebot.TeleBot(key.tg_token, parse_mode='html')


@bot.message_handler(commands=['start'])
def start_mes(message):
    if message.text == '/start':
        # data = func.first_join(message)
        # bot.send_message(message.chat.id, text.start.format(message.from_user.first_name, data[0], data[1]))
        bot.send_message(message.chat.id, 'Пришли смс')


@bot.message_handler(content_types=['voice'])
def voice_process(message):
    name = message.voice.file_id
    info = bot.get_file(name)
    path = info.file_path
    download = bot.download_file(path)
    save_path = 'voices'
    os.makedirs(save_path, exist_ok=True)
    file_name = os.path.join(save_path, f'{name}')
    with open(f'{file_name}.ogg', 'wb') as new_file:
        new_file.write(download)
    time.sleep(2)
    bot.send_message(message.chat.id, "Голосовое сообщение в обработке")
    result = func.voice_rec(name)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text=result)

bot.polling(none_stop=True)