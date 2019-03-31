from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #importar las librerias de telegram
import logging #Genera archivos de log, guarda la parte del historial
import web #importa la libreria web.py

#configura un variable para gardar los sucesos 
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection, conexion a la base de datos
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'demo_bot',
    user = 'utec',
    pw = 'utec.2019',
    port = 3306
    )

#Samm17_bot, poner token
token = '750724286:AAG9rJWkM_RuNzoCXIBmiRkR3ZdxyTD5Zs'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update): #start, hara lo primero que se va a ejecutar.
    username = update.message.from_user.username #Almacenando el nombre de usuario en telegram.
    update.message.reply_text('Busca consejos:\n/ llave #busca_informacion'.format(username)) 
#reply_text mensaje de repuesto. 
def help(bot, update): #helo, consultar ayuda.
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion'.format(username))

def search(update): #search descompone el mensaje, text guarda el mensaje.
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        id_producto = int(text[1]) # cast para convertir str a int, saber que cosas esta buscando el usuario. 1
        print "Send info to {}".format(username)
        print "Key search {}".format(id_producto)
        result = db.select('productos', where='id_producto=$id_producto', vars=locals())[0] # 2Busqueda, vars permite reconocer como variable a id_p
        print result # 3
        respuesta =  str(result.producto) + ", " + str(result.existencias) + ", " + str(result.precio) # 4
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hola {}\nEsta es la informacion que buscas:\n{}'.format(username, respuesta)) #36 a 44 se encarga de dar respuesta al usuario
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(id_producto))

def info(bot, update):
    search(update)

def echo(bot, update): #repite lo que le decimos 
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error): 
    logger.warn('Update "%s" caused error "%s"' % (update, error))
 
def main():
    try:
        print 'S.A.M.M. init token'
        
        updater = Updater(token) #se crea el bot como tal, en caso de error bota y falla.

        # Get the dispatcher to register handlers
        dp = updater.dispatcher #

        print 'S.A.M.M. init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("info", info))        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))
        
        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'S.A.M.M. ready'
        updater.idle() #Pone al bot en modo espera 
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__': #Hacen que se ejecute el bot
    main()
