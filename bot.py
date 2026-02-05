print("Bot is starting...")
BOT_TOKEN = "7860257344:AAGrCYG9cDzX7Vz4aWIrruHhOcFmRSJK3Sc"
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = "7860257344:AAGrCYG9cDzX7Vz4aWIrruHhOcFmRSJK3Sc"  # ← apna BotFather token

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Bot is live 🎉")

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
