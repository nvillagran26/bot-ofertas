import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

usuarios = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    usuarios.add(user_id)
    await update.message.reply_text("Hola! Te enviaré ofertas cuando estén disponibles.")

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

async def enviar_ofertas(application):
    while True:
        mensaje = """
🔥 OFERTAS DEL DIA 🔥

🛍️ Falabella
https://www.falabella.com/falabella-cl

🛍️ Ripley
https://simple.ripley.cl/

💻 SoloTodo
https://www.solotodo.cl/
"""
        for user_id in usuarios:
            try:
                await application.bot.send_message(chat_id=user_id, text=mensaje)
            except:
                pass

        await asyncio.sleep(86400)  # 24 horas

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ofertas", ofertas))

    asyncio.create_task(enviar_ofertas(app))

    print("Bot funcionando...")
    await app.run_polling()

asyncio.run(main())
