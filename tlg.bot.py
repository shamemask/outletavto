# from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


async def wake_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Hell'
    )

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler['start', wake_up])
    app.run_polling()

if __name__ == '__main__':
    main()