import telebot
from telebot import types

TOKEN = "8462024487:AAHwxjk85iauvYtfVRYp9SsgCENpxYE4pEI"
TOKEN = "ضع_التوكن_هنا"
bot = telebot.TeleBot(TOKEN)

# قائمة المواد (مثال)
subjects = ["رياضيات", "إحصاء", "فيزياء", "كيمياء"]

# رسالة البداية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📘 كتب")
    btn2 = types.KeyboardButton("📑 تجميعات")
    btn3 = types.KeyboardButton("📝 ملخصات")
    btn4 = types.KeyboardButton("📚 خصوصي")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(
        message.chat.id,
        "أهلاً بك في بوت جامعة بيشة 🎓\nاختر الخدمة من القائمة:",
        reply_markup=markup
    )

# التعامل مع الخيارات
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    if message.text == "📘 كتب":
        bot.send_message(message.chat.id, "هنا روابط الكتب 📘")
    elif message.text == "📑 تجميعات":
        bot.send_message(message.chat.id, "هنا روابط التجميعات 📑")
    elif message.text == "📝 ملخصات":
        bot.send_message(message.chat.id, "هنا روابط الملخصات 📝")
    elif message.text == "📚 خصوصي":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for sub in subjects:
            markup.add(types.KeyboardButton(sub))
        bot.send_message(message.chat.id, "اختر المادة لحلها خصوصي:", reply_markup=markup)
    elif message.text in subjects:
        bot.send_message(message.chat.id, f"أنت اخترت مادة: {message.text}\nسنضيف خدماتها لاحقاً ✅")
    else:
        bot.send_message(message.chat.id, "من فضلك اختر من القائمة.")

# تشغيل البوت
print("البوت يعمل ...")
bot.polling()
