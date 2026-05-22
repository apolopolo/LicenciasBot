from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# TOKEN desde Render (NO lo pongas aquí en GitHub)
TOKEN = os.getenv("TOKEN")

zona_horaria = "UTC-5"

def convertir(texto):
    texto = texto.upper()

    activo = None
    direccion = None
    tiempo = None

    pares = [
        "EURUSD","GBPUSD","USDJPY","EURJPY",
        "AUDCAD","USDCHF","EURGBP","GBPJPY"
    ]

    for p in pares:
        if p in texto:
            activo = p
            break

    if "CALL" in texto or "BUY" in texto:
        direccion = "CALL"
    elif "PUT" in texto or "SELL" in texto:
        direccion = "PUT"

    for w in texto.split():
        if ":" in w:
            tiempo = w

    if activo and direccion and tiempo:
        return f"""🚀 SEÑAL CONVERTIDA 🚀

Activo: {activo}
Dirección: {direccion}
Hora: {tiempo}
Zona: {zona_horaria}
Expiración: M1"""
    
    return "❌ Señal no válida"

async def mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(convertir(update.message.text))

async def utc3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global zona_horaria
    zona_horaria = "UTC-3"
    await update.message.reply_text("Zona horaria cambiada a UTC-3")

async def utc5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global zona_horaria
    zona_horaria = "UTC-5"
    await update.message.reply_text("Zona horaria cambiada a UTC-5")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("utc3", utc3))
app.add_handler(CommandHandler("utc5", utc5))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje))

print("BOT CONVERSOR ACTIVO")
app.run_polling()
