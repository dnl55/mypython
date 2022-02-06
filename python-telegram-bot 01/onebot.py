import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')

def start_bot(update: Updater, context: CallbackContext):
    print(update)
    mytext = ("""Привет {}.
    Напиши или нажми /start чтоб я снова вывел это сообщение,
    возможно в дальнейшем тут будет что та по полезнее)""".format(update.message.chat.username) )
    update.message.reply_text(mytext)
#Функция где прописано что будет выводиться в чат 
def chat (update: Updater, context: CallbackContext):
    text = update.message.text

#Логирование 
    logging.info(text)

    update.message.reply_text(text)

def main():
    updtr = Updater(settings.TOKEN_TEKEGRAMM)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    #выводит сообщение когда что та пишешь в чат
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started!')
    main()
     
