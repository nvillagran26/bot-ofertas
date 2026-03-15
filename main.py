import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Soy tu bot de ofertas.")

async def ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = """
🔥 OFERTAS DEL DIA 🔥

1️⃣ Audífonos Bluetooth
https://ejemplo.com

2️⃣ Teclado Gamer
https://ejemplo.com

3️⃣ Mouse Gamer
https://ejemplo.com
"""
    await update.message.reply_text(mensaje)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ofertas", ofertas))

print("Bot funcionando...")

app.run_polling()
