import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot("5939141489:AAFqKuoZN-gFMzA1tB6-l3Aq5IicrAlGPUU")


@bot.message_handler(func=lambda _: True)
def handle_message(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
  )
  bot.send_message(chat_id=message.from_user.id,  text=response['choices'][0]['text'])


bot.polling()
