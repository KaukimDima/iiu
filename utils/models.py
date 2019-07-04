import os
from datetime import datetime
from django.shortcuts import redirect

def default_datetime(): return datetime.now()

def upload_path(instance, filename):
	return os.path.join('media/' + str(instance.__class__.__name__).lower() + '/', filename)

def role_required(func):
	def wrapper(request, **kwargs):
		context = {}
		try:
			role = request.user.get_role()
			print(role)
			context['role'] = role
		except:
			pass
		kwargs['context'] = context

		return func(request, **kwargs) 
	return wrapper
