from telethon import TelegramClient, events
import re

# =====================================
# CONFIG TELEGRAM
# =====================================

api_id = 31627477
api_hash = "4d3e9f5a311e68ed2c6b744b1b3d4d42"
telefono = "+51972103504"

# =====================================
# CLIENTE
# =====================================

client = TelegramClient("bot_session", api_id, api_hash)

print("🚀 CONVERSOR DE SEÑALES ACTIVO")

# =====================================
# CONVERSOR SIMPLE 4 FORMATOS
# =====================================

@client.on(events.NewMessage)
async def convertir(event):

    texto = event.raw_text.upper()

    print("\n===================")
    print("SEÑAL RECIBIDA")
    print("===================")
    print(texto)

    activo = None
    direccion = None
    tiempo = None

    # =====================================
    # DETECTAR ACTIVO
    # =====================================

    ativos = [
        "EURUSD",
        "GBPUSD",
        "USDJPY",
        "EURJPY",
        "AUDCAD",
        "USDCHF",
        "EURGBP",
        "GBPJPY"
    ]

    for par in ativos:
        if par in texto:
            activo = par
            break

    # =====================================
    # DETECTAR DIRECCIÓN
    # =====================================

    if "CALL" in texto or "COMPRA" in texto or "BUY" in texto:
        direccion = "CALL"

    if "PUT" in texto or "VENTA" in texto or "SELL" in texto:
        direccion = "PUT"

    # =====================================
    # DETECTAR HORARIO
    # =====================================

    hora = re.search(r'\d{2}:\d{2}', texto)

    if hora:
        tiempo = hora.group()

    # =====================================
    # FORMATO FINAL
    # =====================================

    if activo and direccion and tiempo:

        mensaje_final = f"""
🚀 SEÑAL CONVERTIDA 🚀

📊 ACTIVO: {activo}
⏰ HORA: {tiempo}
📈 DIRECCIÓN: {direccion}
⏳ EXPIRACIÓN: M1
"""

        print(mensaje_final)

        await event.reply(mensaje_final)

    else:

        print("❌ FORMATO NO RECONOCIDO")

# =====================================
# EJECUTAR
# =====================================

client.start(phone=telefono)
client.run_until_disconnected()
