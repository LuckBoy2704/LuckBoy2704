import telebot
from telebot import types
from mem_set import men_sett
from link import link
from read import reading_txt_file
from timing import show_time
from read_token import get_t
def main():
    bot = telebot.TeleBot(get_t())
    print(get_t())
    @bot.message_handler(commands=['start'])
    def start(message):
        print(message)
        (men_sett(bot=bot, message=message, text=['Вас вітає бот по продажі системних блоків','Чим можу допомогти?'], buttons=['Ознайомча_інформація','Характеристика','Перейти до меню']))
        bot.send_message(message.chat.id, text='Yes')
    @bot.message_handler(commands=['exit'])
    def exit_mess(message):

        bot.send_message(message.chat.id,'Time: ')
        bot.send_message(message.chat.id,'Добре')
        bot.stop_polling()
    @bot.message_handler(content_types=['text'])
    def options(message):
        if message.text == 'Перейти до меню':
            men_sett(bot=bot,message=message, text=['Оберіть категорію:'],
                     buttons=['Моделі','Ціна','Наявність','Повернутися'])
        elif message.text == 'Повернутися':
            men_sett(bot=bot,message=message, text=['Добре'],buttons=['Ознайомча_інформація','Характеристика','Перейти до меню'])
        elif message.text == 'Ознайомча_інформація':
            men_sett(bot=bot,message=message, text=['Відео для розуміння:'],
                     buttons=['Відео'])
        elif message.text in ['Відео']:
            link(message)
        elif message.text == 'Ціна':
            men_sett(bot=bot,message=message, text=['Яка ціна вам підійде?'],
                     buttons=['Дорогий', 'Середній', 'Дешевий', 'Назад'])
        elif message.text == 'Дорогий':
            men_sett(bot=bot,message=message, text=['Підійдуть ці варіанти'],
                     buttons=['COBRA_Gaming', 'AMD Ryzen 5', 'Назад'])
        elif message.text == 'Середній':
            men_sett(bot=bot,message=message, text=['Підійдуть ці варіанти'],
                     buttons=['ARTLINE Gaming', 'HP Pro 290', 'Назад'])
        elif message.text == 'Дешевий':
            men_sett(bot=bot,message=message, text=['Підійдуть ці варіанти'],
                     buttons=['COBRA Advanced', 'Tower NEW', 'Назад'])
        elif message.text == 'Характеристика':
            men_sett(bot=bot, message=message, text=['Інформація по процесорі:','Інформація по відеокарті'],
                     buttons=['Відеокарта', 'Процесор', 'Назад'])
        elif message.text in ['Процесор', 'Відеокарта']:
            link(message)
        elif message.text == 'Моделі':
            men_sett(bot=bot,message=message, text=['Оберіть модель:'],
                     buttons=['COBRA_Gaming', 'ARTLINE Gaming', 'COBRA Advanced', 'AMD Ryzen 5',
                              'Tower NEW', 'HP Pro 290', 'Наявність', 'Назад'])
        elif message.text == 'Наявність':
            men_sett(bot=bot,message=message, text=['В наявності ще буде певний час'],
                     buttons=['Повернутися_до_критерій'])
        elif message.text in ['COBRA_Gaming', 'ARTLINE Gaming', 'COBRA Advanced', 'AMD Ryzen 5', 'Tower NEW', 'HP Pro 290']:
            link(message)
        elif message.text == 'Назад':
            men_sett(bot=bot,message=message, text=['Добре'],
                     buttons=['Моделі', 'Ціна', 'Наявність'])
        elif message.text == 'Повернутися_до_критерій':
            men_sett(bot=bot,message=message, text=['Добре'],
                     buttons=['Ознайомча_інформація','Характеристика','Моделі','Ціна','Наявність'])
    bot.polling(none_stop=True)
if __name__ == "__main__":
    main()
