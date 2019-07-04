from django.core.mail import send_mail
from django.template.loader import render_to_string

def default_send(title, subject, sender, template, context, to ):

    msg_html = render_to_string(template, context )
    send_mail(title, subject, sender, [to], html_message=msg_html)


def new_user(name, phone, id, to):

    context = {
        'name' : name,
        'phone' : phone,
        'id' : id
    }

    default_send(
        'Был зарегистрирован новый пользователь',
        'new user',
        'knewit@info.kz',
        'email/new_user.html',
        context,
        to
    )
