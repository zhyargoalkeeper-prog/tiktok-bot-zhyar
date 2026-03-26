import telebot
import requests

API_TOKEN = '8783123046:AAHQqjrfJZjp3p_87blmPDkIQnQfENbWZKY' 
CHANNEL_ID = '@tiki12332' 

bot = telebot.TeleBot(API_TOKEN)

def check_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"سڵاو! بۆ بەکارهێنانی بۆتەکە، دەبێت جۆینی کەناڵەکە بیت:\n{CHANNEL_ID}\n\nئینجا لینکی تیکتۆک بنێرە.")

@bot.message_handler(func=lambda message: 'tiktok.com' in message.text)
def download_tiktok(message):
    user_id = message.from_user.id
    if not check_user_joined(user_id):
        bot.send_message(message.chat.id, f"⚠️ سەرەتا جۆین بە: {CHANNEL_ID}")
        return

    url = message.text
    bot.send_message(message.chat.id, "خەریکی دابەزاندنم... 🚀")
    try:
        # بەکارهێنانی API جیاواز بۆ دڵنیایی زیاتر
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()
        video_url = response['data']['play']
        bot.send_video(message.chat.id, video_url, caption="فەرموو ڤیدیۆکەت! ✅\n\n@tiki12332")
    except:
        bot.reply_to(message, "ببورە، کێشەیەک لە سێرڤەری تیکتۆک هەبوو.")

bot.polling()
