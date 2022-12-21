import json


api_sessions = dict()

with open('replies.json', 'r', encoding='utf-8') as f:
    replies = json.load(f)

def process(user, text):
    global api_sessions

    chosen_reply = None

    for reply in replies:
        for key in replies[reply]['keywords']:
            if text.startswith(key):
                chosen_reply = reply
                break

    if chosen_reply is None:
        return "Простите, я не понимаю вас"

    return replies[chosen_reply]["answer"]

