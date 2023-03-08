import requests

def telegram_bot_sendtext(bot_message):

   bot_token = "6180022751:AAGw7HN_ry3XOWLPI4aD25WrfS-ODhq2L1E"
   bot_chatID = '5566967126'
   send_text = 'https://api.telegram.org/bot' + bot_token \6180022751:AAGw7HN_ry3XOWLPI4aD25WrfS-ODhq2L1E
      + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' \
      + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
