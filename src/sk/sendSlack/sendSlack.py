import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-974853239138-1873692512450-PMPTmlDdZTxmi6NFgw6zHSsz"
 
post_message(myToken,"#python-auto-trader","Hi~ my name is sk")
