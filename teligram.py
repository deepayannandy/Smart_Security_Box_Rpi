from telegram.ext import *
import constants as keys

print("Bot Started....")

def start_command(update,context):
	update.message.reply_text("Hello this is DNYIndia's Chat Bot")

def help_command(update, context):
	update.message.reply_text('Contact: 7384213622')
def hendel_message(update, context):
	text=str(update.message.text).lower()
	if text=="subscribe":
		update.message.reply_text("Click on this: /get_id \n to generate the Chat id")
	else:
		update.message.reply_text("I am not programme to answer this!")
def chat_id_command(update,context):
	id=str(update.message.chat.id)
	update.message.reply_text("Your Caht id is: "+id)
def errot(update,context):
	print(update,context)

def main():
	updater=Updater(keys.API_Key,use_context=True)
	dp=updater.dispatcher

	dp.add_handler(CommandHandler('start',start_command))
	dp.add_handler(CommandHandler('help',help_command))
	dp.add_handler(CommandHandler('get_id',chat_id_command))
	dp.add_handler(MessageHandler(Filters.text,hendel_message))

	updater.start_polling()
	updater.idle()

main()