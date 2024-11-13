from read import reading_txt_file
from mem_set import men_sett
import telebot
bot = telebot.TeleBot('7666894807:AAHPmYTRtS0OOwAv1Begxw38oEYIVu2GoYI')
def link(message):
    url = reading_txt_file(message.text)
    if url:
        bot.send_message(message.chat.id, text=[f'Посилання на {message.text}: {url}'])
    men_sett(bot,message, text=['Непоганий варіант'], buttons=['Назад'])
