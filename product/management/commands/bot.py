import telebot
from telebot import types
from django.core.management.base import BaseCommand

bot = telebot.TeleBot("8481516173:AAERNwHLyEeycaonXLL20yJ3tBuDOUJQw8g", parse_mode=None)

class Command(BaseCommand):

    def handle(self, *args, **options):

        @bot.message_handler(commands=["start"])
        def start(message):
            bot.send_message(message.chat.id, "Добро пожаловать")
        
        @bot.message_handler(commands=["privet"])
        def say_hello(message):
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(
                "Нажми на меня",
                callback_data="target"
            )
            keyboard.add(button1)
            bot.send_message(message.chat.id, "Привет", reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: call.data == "target")
        def callback_hello(call):
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "Молодец")
            
        bot.infinity_polling()

