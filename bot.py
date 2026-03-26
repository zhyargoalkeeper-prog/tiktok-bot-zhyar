import telebot
import requests

# تۆکنە ڕاستەکەت
API_TOKEN = '8783123046:AAHQqjrfJZjp3p_87blmPDkIQnQfENbWZKY' 

# یوزەرنەیمی کەناڵەکەت کە لە وێنەکەدا دیارە
CHANNEL_ID = '@tiki12332' 

bot = telebot.TeleBot(API_TOKEN)

def check_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        return False
    except:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"سڵاو! بۆ بەکارهێنانی بۆتەکە، دەبێت سەرەتا جۆینی کەناڵەکەمان بیت:\n{CHANNEL_ID}\n\nدوای ئەوە لینکی ڤیدیۆی تیکتۆکم بۆ بنێرە. 🚀")

@bot.message_handler(func=lambda message: 'tiktok.com' in message.text)
def download_tiktok(message):
    user_id = message.from_user.id
    
    # پشکنینی ئەوەی ئایا جۆینی کەناڵەکەیە؟
    if not check_user_joined(user_id):
        bot.send_message(message.chat.id, f"⚠️ ببورە! بۆ ئەوەی بتوانیت ڤیدیۆ دابەزێنیت، دەبێت سەرەتا جۆینی کەناڵەکەمان بیت: \n\n {CHANNEL_ID}")
        return

    url = message.text
    bot.send_message(message.chat.id, "خەریکی دابەزاندنم... تکایە چاوەڕوان بە 🚀")
    try:
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()
        video_url = response['data']['play']
        bot.send_video(message.chat.id, video_url, caption="فەرموو ڤیدیۆکەت ئامادەیە! ✅\n\n@tiki12332")
    except:
        bot.reply_to(message, "ببورە، کێشەیەک لە دابەزاندنی ڤیدیۆکە هەبوو.")

print("بۆتەکە ئێستا بە مەرجی جۆین کردن چالاکە...")
bot.polling()