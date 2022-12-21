from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from logic import process
import vk_api
import os
import random


_session = None

def get_session():
    global _session
    if _session:
        return _session
    _session = vk_api.VkApi(token=os.environ.get("TOKEN"))
    return _session

def send(user, text):
    vk = get_session().get_api()
    vk.messages.send(user_id=user,
                     message=text,
                     random_id=random.randint(0, 2 ** 64))

def run():
    print(os.environ.get("TOKEN"))
    longpoll = VkBotLongPoll(get_session(), group_id=os.environ.get("GROUP_ID"))

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user = event.obj.message['from_id']
            text = event.obj.message['text']

            reply = process(user, text)
            send(user, reply)
            
