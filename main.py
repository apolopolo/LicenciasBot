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
