import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

usuarios = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    usuarios.add(user_id)
    await update.message.reply_text("Hola! Soy tu bot de ofertas.")

async def ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = """
🔥 OFERTAS DEL DIA 🔥

🛍️ Falabella
https://www.falabella.com/falabella-cl

🛍️ Ripley
https://simple.ripley.cl/

💻 SoloTodo
https://www.solotodo.cl/
"""
    await update.message.reply_text(mensaje)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ofertas", ofertas))

print("Bot funcionando...")

app.run_polling()
