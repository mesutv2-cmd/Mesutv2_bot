import telebot
from telebot import types
import time

TOKEN = "7978432031:AAEvlV2YdHKfb_Mxn3sY00OeaRYXnxvPnxs"
ADMIN_ID = 261010597 
CH_ID = -1003859418824 
CH_URL = "https://t.me/+XgF2ld7uma8zMTdk"

bot = telebot.TeleBot(TOKEN)

def is_member(user_id):
    try:
        status = bot.get_chat_member(CH_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except: return True

@bot.message_handler(commands=['start'])
def start(m):
    if not is_member(m.from_user.id):
        kb = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("📢 عضویت در کانال", url=CH_URL))
        kb.add(types.InlineKeyboardButton("✅ عضو شدم", callback_data="check"))
        bot.send_message(m.chat.id, f"⚠️ سلام {m.from_user.first_name} عزیز!\nبرای استفاده از ربات، ابتدا در کانال عضو شوید:", reply_markup=kb)
        return
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('🚀 دریافت کانفیگ V2ray', '🛡 دریافت پروکسی تلگرام')
    markup.add('📥 دانلود برنامه‌ها', '📚 راهنمای اتصال')
    bot.send_message(m.chat.id, f"✅ سلام {m.from_user.first_name} عزیز، منو فعال شد:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):
    if is_member(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)
    else:
        bot.answer_callback_query(call.id, "❌ هنوز عضو نشدید!", show_alert=True)

@bot.message_handler(func=lambda m: True)
def handle(m):
    if not is_member(m.from_user.id):
        start(m)
        return

    if 'دریافت کانفیگ' in m.text:
        v1 = "vless://f3d15446-946d-4333-9f1e-441a5399b7a8@h47.tiptop-3.top:50709?security=none&encryption=none&host=speedtest.net&headerType=http&type=tcp#h33-Mesutv2NEW-1"
        v2 = "vless://f1b8e374-fa3e-5efb-93d7-dd595de25ee3@dl.bookpersianenghlish.com:40398?security=none&encryption=none&headerType=none&type=tcp#mesut-4-Mesutv2NEW-1004"
        bot.send_message(m.chat.id, f"🚀 **کانفیگ‌های شما:**\n\n1️⃣ `{v1}`\n\n2️⃣ `{v2}`", parse_mode='Markdown')
    
    elif 'پروکسی' in m.text:
        bot.send_message(m.chat.id, "🛡 [اتصال به پروکسی](https://t.me/proxy?server=85.133.194.121&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ)", parse_mode='Markdown')

    elif 'دانلود' in m.text:
        bot.send_message(m.chat.id, "📥 [v2rayNG Android](https://play.google.com/store/apps/details?id=com.v2ray.ang)\n📥 [V2Box iOS](https://apps.apple.com/us/app/v2box-v2ray-client/id1640130422)", parse_mode='Markdown')

while True:
    try: bot.polling(none_stop=True)
    except: time.sleep(15)
