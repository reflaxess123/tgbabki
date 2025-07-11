import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, _):
    if update.message:
        await update.message.reply_text("Привет я твой пидар ибаный!")

async def help_command(update: Update, _):
    if update.message:
        await update.message.reply_text("Доступные команды: /start /help")

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN не найден")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
