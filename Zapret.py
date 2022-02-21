import telebot;
import random
from PIL import Image, ImageDraw,ImageFont
bot = telebot.TeleBot('5171559198:AAEZGlQpigDaEcgZWAMlukFKaAp41GS1uRA')
@bot.message_handler( commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message( message.chat.id, "Введите:Запрети")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    im = Image.open('Zapret.jpg')
    f= open('1.txt', encoding="utf8")
    p = []
    for line in f:
        p.append(line)      
    font = ImageFont.truetype('gilroy-black.ttf', size=20)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
    (10, 150),
    p[random.randint(0, len(p))].lower(),
    # Добавляем шрифт к изображению
    font=font,
    fill='#1C0606')
    im.save('new_pic.jpg')
    photo=open('new_pic.jpg', 'rb')
    if message.text.lower() == "запрети":
        bot.send_photo( message.chat.id,photo)
bot.polling(none_stop=True, interval=0)    

