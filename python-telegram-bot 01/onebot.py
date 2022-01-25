from telegram.ext import Updater, CommandHandler, CallbackContext

def start_bot(update: Updater, context: CallbackContext):
    mytext = ("""Привет {}.
    Напиши или нажми /start чтоб я снова вывел это сообщение,
    возможно в дальнейшем тут будет что та по полезнее)""".format(update.message.chat.first_name) )
    update.message.reply_text(mytext)

def main():
    updtr = Updater("1985672039:AAF-uV6oITqeCiLR7ADTlxBlALYROTTuKCg")

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    main()
     
