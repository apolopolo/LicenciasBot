from telethon import TelegramClient, events

# =========================
# CONFIGURACIÓN TELEGRAM
# =========================

api_id = 12345678
api_hash = "TU_API_HASH"
telefono = "+51999999999"

# Canal origen
canal_entrada = "CANAL_ORIGEN"

# Canal destino
canal_salida = "CANAL_DESTINO"

# =========================
# INICIAR CLIENTE
# =========================

client = TelegramClient("session_bot", api_id, api_hash)

# =========================
# CONVERSOR DE SEÑALES
# =========================

@client.on(events.NewMessage(chats=canal_entrada))
async def convertir_signal(event):

    mensaje = event.raw_text

    print("\n========================")
    print("SEÑAL RECIBIDA")
    print("========================")
    print(mensaje)

    # =========================
    # CONVERSIÓN SIMPLE
    # =========================

    nuevo_mensaje = mensaje.upper()

    # =========================
    # ENVIAR
    # =========================

    await client.send_message(
        canal_salida,
        f"🚀 SEÑAL CONVERTIDA 🚀\n\n{nuevo_mensaje}"
    )

    print("SEÑAL ENVIADA")

# =========================
# EJECUTAR BOT
# =========================

print("BOT CONVERSOR ACTIVO...")

client.start(phone=telefono)
client.run_until_disconnected()
