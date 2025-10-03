# bot.py
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print("🎉 محیط VS Code آماده است!")

# 🔑 توکن شما - اینجا قرار بدید
BOT_TOKEN = "7264777877:AAFpFjJ9IgtkFX3kSVJh-ZSTL4T3PYbotrw"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /start"""
    await update.message.reply_text("سلام! به ربات من خوش آمدید! 🤖")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /help"""
    help_text = """
📖 راهنمای ربات:

/start - شروع کار
/help - نمایش این راهنما

یا مستقیم پیام بفرستید تا پاسخ دهم!
    """
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """پردازش پیام‌های کاربر"""
    user_message = update.message.text
    user_name = update.message.from_user.first_name
    
    response = f"سلام {user_name}! 👋\nشما گفتید: {user_message}"
    await update.message.reply_text(response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """مدیریت خطاها"""
    print(f"⚠️ خطا رخ داد: {context.error}")

def main():
    """تابع اصلی"""
    print("🚀 در حال راه‌اندازی ربات تلگرامی...")
    
    # ساخت اپلیکیشن
    application = Application.builder().token(BOT_TOKEN).build()
    
    # اضافه کردن دستورات
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    
    # اضافه کردن هندلر پیام‌ها
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # هندلر خطا
    application.add_error_handler(error_handler)
    
    print("✅ ربات آماده است!")
    print("📱 به تلگرام برید و بات رو تست کنید...")
    print("⏹️ برای توقف: Ctrl + C")
    
    # شروع بات
    application.run_polling()

if __name__ == '__main__':
    main()