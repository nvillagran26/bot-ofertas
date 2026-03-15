import os
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# PON AQUI EL ID DE TU CANAL
CANAL_ID = -1003797588613


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        ["🔥 Ver ofertas"],
        ["🛍️ Tiendas", "💻 Tecnología"]
    ]

    reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)

    await update.message.reply_text(
        "Bienvenido al Bot de Ofertas 👋\nSelecciona una opción:",
        reply_markup=reply_markup
    )


async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = update.message.text

    if texto == "🔥 Ver ofertas":

        mensaje = """
🔥 OFERTAS DEL DIA 🔥

🛍️ Falabella
https://www.falabella.com/falabella-cl

🛍️ Ripley
https://simple.ripley.cl/

💻 SoloTodo
https://www.solotodo.cl/
"""

        await update.message.reply_text(mensaje, disable_web_page_preview=True)

    elif texto == "🛍️ Tiendas":

        mensaje = """
🛍️ TIENDAS

Falabella
https://www.falabella.com

Ripley
https://simple.ripley.cl
"""

        await update.message.reply_text(mensaje, disable_web_page_preview=True)

    elif texto == "💻 Tecnología":

        mensaje = """
💻 OFERTA TECNOLOGÍA

🖱️ Mouse Gamer Logitech G203
💰 Precio aprox: $9.990

💻 Comparar precios
https://www.solotodo.cl/products/6901-logitech-g203-lightsync-black
"""

        await update.message.reply_text(mensaje, disable_web_page_preview=True)


async def publicar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensaje = """
🔥 OFERTA

🛍️ Falabella
https://www.falabella.com/falabella-cl

🛍️ Ripley
https://simple.ripley.cl/

💻 SoloTodo
https://www.solotodo.cl/
"""

    await context.bot.send_message(
        chat_id=CANAL_ID,
        text=mensaje,
        disable_web_page_preview=True
    )

    await update.message.reply_text("Oferta publicada en el canal ✅")


async def tecnologia(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensaje = """
🔥 OFERTA TECNOLOGÍA

🖱️ Mouse Gamer Logitech G203
💰 Precio aprox: $9.990

💻 Comparar precios
https://www.solotodo.cl/products/6901-logitech-g203-lightsync-black
"""

    await context.bot.send_message(
        chat_id=CANAL_ID,
        text=mensaje,
        disable_web_page_preview=True
    )

    await update.message.reply_text("Oferta publicada en el canal ✅")


async def publicar_automatico(application):

    while True:

        mensaje = """
🔥 OFERTA AUTOMÁTICA

🛍️ Falabella
https://www.falabella.com/falabella-cl

🛍️ Ripley
https://simple.ripley.cl/

💻 SoloTodo
https://www.solotodo.cl/
"""

        await application.bot.send_message(
            chat_id=CANAL_ID,
            text=mensaje,
            disable_web_page_preview=True
        )

        await asyncio.sleep(3600)  # 1 hora


async def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("publicar", publicar))
    app.add_handler(CommandHandler("tecnologia", tecnologia))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    asyncio.create_task(publicar_automatico(app))

    print("Bot funcionando...")

    await app.run_polling()


asyncio.run(main())
