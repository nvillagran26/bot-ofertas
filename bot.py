from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import requests
from bs4 import BeautifulSoup

TOKEN = "8625631973:AAFPrN4O6xfuUdrs0I64G8QsNGiemAvUYyI"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola 👋 Soy tu bot de ofertas")


def obtener_ofertas():

    url = "https://fakestoreapi.com/products"

    respuesta = requests.get(url)

    productos = respuesta.json()

    mensaje = ""

    for producto in productos[:5]:

        nombre = producto["title"]
        precio = producto["price"]

        mensaje += f"{nombre}\n💰 ${precio}\n\n"

    return mensaje


async def ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = obtener_ofertas()

    await update.message.reply_text(texto)


def obtener_ofertas_chile():

    url = "https://www.solotodo.cl/notebooks"

    headers = {"User-Agent": "Mozilla/5.0"}

    respuesta = requests.get(url, headers=headers)

    soup = BeautifulSoup(respuesta.text, "html.parser")

    enlaces = soup.find_all("a")

    mensaje = "💻 Ofertas encontradas:\n\n"

    contador = 0

    for e in enlaces:

        texto = e.get_text().strip()

        if len(texto) > 20:

            mensaje += texto + "\n\n"
            contador += 1

        if contador == 5:
            break

    return mensaje


async def chile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    texto = obtener_ofertas_chile()

    await update.message.reply_text(texto)


async def enviar_ofertas(context: ContextTypes.DEFAULT_TYPE):

    texto = obtener_ofertas()

    chat_id = context.job.chat_id

    await context.bot.send_message(chat_id=chat_id, text=texto)


async def activar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    context.job_queue.run_repeating(
        enviar_ofertas,
        interval=1800,
        first=10,
        chat_id=chat_id
    )

    await update.message.reply_text("🔔 Alertas de ofertas activadas")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ofertas", ofertas))
app.add_handler(CommandHandler("chile", chile))
app.add_handler(CommandHandler("alertas", activar))

print("Bot funcionando...")

app.run_polling()
