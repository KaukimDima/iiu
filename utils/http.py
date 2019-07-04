from frontend.models import (
    Advantage, 
    Contacts,
    Social
) 
from functools import wraps

def base_data():
    """
    Decorator to make a view only accept request with required parameters.
    :param parameters_list: list of required parameters.
    """
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            context = {}

            advantages = Advantage.objects.filter(active=True)
            contacts = Contacts.objects.filter(active=True)
            socials = Social.objects.filter(active=True)
            context.update({
                'advantages' : advantages,
                'contacts' : contacts, 
                'socials' : socials, 

            })
            kwargs['context'] = context

            return func(request, *args, **kwargs)
        return inner
    return decorator


def get_telegram_data(data):
    telegram_data = data['originalDetectIntentRequest']['payload']\
            ['data']['message']['chat']

    return {
        'name': telegram_data.get('username'), 
        'id' : telegram_data.get('id')
    }
def get_t_callback(data):
    telegram_data = data['originalDetectIntentRequest']['payload']\
        ['data']['callback_query']['from']

    return {
        'name': telegram_data.get('username'), 
        'id' : telegram_data.get('id')
    }

def get_query_text(data):
    
    return data['queryResult']['queryText']
