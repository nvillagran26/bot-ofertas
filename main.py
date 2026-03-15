import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ID DE TU CANAL
CANAL_ID = -1003797588613


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        ["🔥 Ver ofertas"],
        ["🛍️ Tiendas", "💻 Tecnología"]
    ]

    reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)

    await update.message.reply_text(
        "Bienvenido al Bot de Ofertas 👋",
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

        await update.message.reply_text(
            mensaje,
            disable_web_page_preview=True
        )

    elif texto == "🛍️ Tiendas":

        mensaje = """
🛍️ TIENDAS

Falabella
https://www.falabella.com

Ripley
https://simple.ripley.cl
"""

        await update.message.reply_text(
            mensaje,
            disable_web_page_preview=True
        )

    elif texto == "💻 Tecnología":

        mensaje = """
💻 OFERTA TECNOLOGÍA

🖱️ Mouse Gamer Logitech G203
💰 Precio aprox: $9.990

💻 Comparar precios
https://www.solotodo.cl/products/6901-logitech-g203-lightsync-black
"""

        await update.message.reply_text(
            mensaje,
            disable_web_page_preview=True
        )


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


# PUBLICACIÓN AUTOMÁTICA CADA 1 HORA
async def ofertas_automaticas(context: ContextTypes.DEFAULT_TYPE):

    mensaje = """
🔥 OFERTA AUTOMÁTICA

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


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("publicar", publicar))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    # PUBLICAR CADA 1 HORA (3600 segundos)
    app.job_queue.run_repeating(ofertas_automaticas, interval=3600, first=10)

    print("Bot funcionando...")

    app.run_polling()


if __name__ == "__main__":
    main()
