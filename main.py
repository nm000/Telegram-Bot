from telegram.ext import Updater, CommandHandler

#LEE EL ARCHIVO CON LA CLAVE DADA POR EL BotFather
with open('keyBot.txt', 'r') as f:
    KEY = f.read()

#Comandos claves del bot
def start(actualizador, contexto):
    actualizador.message.reply_text("SOY UN BOT")

def content(actualizador, contexto):
    actualizador.message.reply_text("Acá lo del método del Cesar")

def contact(actualizador, contexto):
    actualizador.message.reply_text(""""
    GMAIL UNINORTE:
    Líder: sonyac@uninorte.edu.co
    Miembro 1: npmendoza@uninorte.edu.co
    Miembro 2: yulissam@uninorte.edu.co
    """)

def help(actualizador, contexto):
    actualizador.message.reply_text("""
    COMANDOS:
    /start -> Bienvenida
    /help -> Este menú
    /content -> Información sobre mí - el BOT -
    /contact -> Información de contacto
    /codificarTexto -> Codifica, por el método de cifrado del César, un texto ingresado
    /decodificarTexto -> Decodifica, por el método de cifrado del César, un texto ingresado
    """)

def codificarTexto(actualizador, contexto):
    actualizador.message.reply_text("PRÓXIMAMENTE: podrás codificar aquellos mensajes que ingreses")

def decodificarTexto(actualizador, contexto):
    actualizador.message.reply_text("PRÓXIMAMENTE: podrás decodificar aquellos mensajes que ingreses")

#Permite que el bot ande, usando como servidor local el computador
actualizador = Updater(KEY, use_context = True)

#para aceptar los comandos
disp = actualizador.dispatcher

disp.add_handler(CommandHandler("start", start))
disp.add_handler(CommandHandler("content", content))
disp.add_handler(CommandHandler("help", help))
disp.add_handler(CommandHandler("contact", contact))
disp.add_handler(CommandHandler("codificarTexto", codificarTexto))
disp.add_handler(CommandHandler("decodificarTexto", decodificarTexto))

actualizador.start_polling()
actualizador.idle()

