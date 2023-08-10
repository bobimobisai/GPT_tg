import telebot
import openai
import os

#insert your telegram bot token
bot = telebot.TeleBot('your telegram bot token')
#insert your telegram id, to access the bot, the id can be obtained by typing @my_id_bot
allowed_user_ids = [123456789]
#your token from open ai
openai.api_key = "ab-cdcd1234567890exampl"
context = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "your text is any, for fun)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('random button option')
    itembtn2 = telebot.types.KeyboardButton('random button option')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "choose an answer:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id in allowed_user_ids:
        prompt = message.text
        context.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", #your version of the open ai model
            messages=context
        )
        bot_response = response.choices[0].message.content
        context.append({"role": "assistant", "content": bot_response})
        bot.send_message(message.chat.id, bot_response)
    else:
        bot.send_message(message.chat.id, "It looks like your telegram ID is not in the wight list, write @exampl if you want me to work") #you can change the text, this is an example

bot.polling()
