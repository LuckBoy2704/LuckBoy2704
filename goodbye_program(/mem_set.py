import telebot
from timing import show_time


@show_time
def men_sett(bot,message,text,buttons):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for item in buttons:
        button = telebot.types.KeyboardButton(item)
        keyboard.add(button)
    for t in text:
        bot.send_message(message.chat.id, t, reply_markup=keyboard)
