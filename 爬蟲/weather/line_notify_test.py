import requests
def line_notify():
  token = 'gTDR3X2Qn6RJ2kdpFI0DQSBKKfC0Qs6pUWGKLN1E0G2'
  message = "may you have a wonderful day!"
  url = "https://notify-api.line.me/api/notify"

  payload = {
    "message" : message,
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + token
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
  
  print(response.status_code)

if __name__ == "__main__":
  line_notify()
else:
  print("not sending message")