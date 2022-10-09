import vk_api, json
import re
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_tokens import vk_token
from ParaNET import ParaNETmodel
vk_session = vk_api.VkApi(token=vk_token)
bot = vk_session.get_api()
longpull = VkLongPoll(vk_session)

paraNET = ParaNETmodel()


def msg_send(id, text):
    bot.messages.send(user_id = id,
                      message = text,
                      random_id = 0)


def chat_msg(id,text):
    vk_session.method('messages.send',{'chat_id':id, 'message':text, 'random_id': 0})

for event in longpull.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        if event.from_chat:
            msg = event.text.lower()
            id = event.chat_id
            answer = paraNET.msg_Analise(msg)
            chat_msg(id, 'Тут должен быть раздел: ' + answer)
        else:

            msg = event.text

            id = event.user_id
            if msg.lower() == 'спасибо!' or msg.lower() == 'спасибо':
                msg_send(id,'Всегда пожалуйста!')
            elif msg.lower() == 'привет' or msg.lower() == 'здравствуйте' or msg.lower() == 'начать':
                msg_send(id, 'Приветствую, меня зовут ParaNET! Я местный искуссвенный интеллект, помогающий найти информацию \nНапиши свой вопрос и я постараюсь найти на него ответ!')
                print('1')
            else:
                answer = paraNET.msg_Analise(msg)
                print(msg+'  '+answer)
                msg_send(id,'Тут должен быть раздел: ' + answer)

