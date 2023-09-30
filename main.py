import telebot
from telebot import types

bot = telebot.TeleBot('6513610769:AAE5TNK4hdsVUDdpYXhudTkgazQnzrRlNw8')

@bot.message_handler()
def user_text(message):
    if message.text=='Понедельник':
        bot.send_message(message.chat.id,'1 РОВ 8.30-9.10\n2 Английский 9.20 - 10.00\n3 Литература 10.20 - 11.00\n4 Физика 11.20 - 12.00\n5 Родная Литература 12.00 - 13.00\n6 Математика 13.10 - 13.50\n7 Математика 14.00 - 14.40')
    elif message.text=='Вторник':
        bot.send_message(message.chat.id,'1 История 8.30-9.10\n2 Русский яз. 9.20 - 10.00\n3 Литература 10.20 - 11.00\n4 Английский 11.20 - 12.00\n5 История 12.00 - 13.00\n6 Информатика 13.10 - 13.50\n7 Информатика 14.00 - 14.40')
    elif message.text=='Среда':
        bot.send_message(message.chat.id,'1 Математика 8.30-9.10\n2 Математика 9.20 - 10.00\n3 Английский 10.20 - 11.00\n4 Литература 11.20 - 12.00\n5 Теория вероятности 12.00 - 13.00\n6 Русский яз. 13.10 - 13.50\n7 Физ-ра 14.00 - 14.40')
    elif message.text=='Четверг':
        bot.send_message(message.chat.id,'1 ОБЖ 8.30-9.10\n2 Физика 9.20 - 10.00\n3 Обществознание 10.20 - 11.00\n4 Математика 11.20 - 12.00\n5 Математика 12.00 - 13.00\n6 Информатика 13.10 - 13.50\n7 Информатика 14.00 - 14.40')
    elif message.text=='Пятница':
        bot.send_message(message.chat.id,'1 Химия 8.30-9.10\n2 Физ-ра 9.20 - 10.00\n3 Физ-ра 10.20 - 11.00\n4 География 11.20 - 12.00\n5 Биология 12.00 - 13.00\n6 Русский яз. 13.10 - 13.50\n7 Математика 14.00 - 14.40')
    elif message.text=='easteregg':
        bot.send_message(message.chat.id,'Пасхалка!!! Если ты это нашел напиши Nupox-у "Шампунь жумайсынба"')



bot.infinity_polling()