import requests


def send_alart(id,message):
	try:
		path=f"https://api.telegram.org/bot1068445966:AAGUxOgEp5Kd-87gfiUs9cIFrr5gqbAL2tQ/sendMessage?chat_id={id}&text={message}"
		response = requests.get(path)
		print("sent")
	except:
		print("Something Went Wrong")


send_alart('902935178',"hi")