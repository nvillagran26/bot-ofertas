import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
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
        await update.message.reply_text(mensaje)
        
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
    await context.bot.send_message(chat_id=CANAL_ID, text=mensaje)
    await update.message.reply_text("Oferta publicada en el canal ✅")

    elif texto == "🛍️ Tiendas":
        mensaje = """
🛍️ TIENDAS

Falabella  
https://www.falabella.com

Ripley  
https://simple.ripley.cl
"""
        await update.message.reply_text(mensaje)

    elif texto == "💻 Tecnología":
        mensaje = """
💻 TECNOLOGÍA

SoloTodo  
https://www.solotodo.cl
"""
        await update.message.reply_text(mensaje)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("publicar", publicar))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

print("Bot funcionando...")

app.run_polling()
