import requests
import json

def add_image(url):

    return {
        "image": {
            "imageUri": url
        },
        "platform": "TELEGRAM"
    }


def add_card(subtitle, title, img_url, buttons):

    buttons = []

    for x in buttons:
        obj = {'text': x[0]}
        if x[1]: 
            obj['postback'] = x[1]
        buttons.append(
            obj
        )

    return {
        "card": {
            "subtitle": subtitle,
            "buttons": buttons,
            "imageUri": img_url, 
            "title": title
        },
        "platform": "TELEGRAM"
    }


def add_visual_btns(title, data):

    return {
        "payload": {
            "telegram": {
                "reply_markup": {
                    "inline_keyboard": [
                        [{"text": x[0], "callback_data": x[1]}] for x in data
                    ]
                },
                "text": title
            }
        },
        "platform": "TELEGRAM"
    }


def add_quick_reply(title, answers):

    return {
        "platform": "TELEGRAM",
        "quickReplies": {
            "quickReplies": [x for x in answers], 
            "title": title
            }
    }



def send_m_t_user( t_id, bot_t, text, buttons=None ):
    
    method = 'sendMessage'

    data = { 
        'chat_id': t_id,   
        'text': text,
    }

    if buttons:

        inline = {
            "inline_keyboard": [
                [
                    {"text": x[0], "callback_data": x[1]}\
                        for x in buttons
                ] 
            ]
        }
        
        data['reply_markup'] = json.dumps(inline)



    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(bot_t, method),
        data=data
    ).json()
