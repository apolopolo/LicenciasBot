import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN = "8853301534:AAFd0x0CAfeaUTvh8GpVvQ0LsNhz_w66erg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot activo 🚀")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Recibido: {update.message.text}")

def main():
    try:
        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
        )

        print("BOT INICIANDO...")
        app.run_polling()

    except Exception as e:
        print("ERROR REAL:")
        print(e)

if __name__ == "__main__":
    main()
