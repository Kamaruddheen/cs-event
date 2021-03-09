from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

def is_admin(function):
	def wrap(request,*args,**kwargs):
		if request.user.is_authenticated:
			if request.user.user_type == 1:
				return function(request,*args,**kwargs)
			else:
				messages.info(request,'Not Authorized')
				prev_url = request.META.get('HTTP_REFERER')
				cur_url = request.get_full_path()
				print(prev_url)
				if prev_url:
					redirect_url = 'homepage' if cur_url in prev_url else prev_url
				else:
					redirect_url = 'homepage'
				print(redirect_url)
				return redirect(redirect_url or 'homepage',)
		else:
			return redirect(redirect('login').url+'?next='+request.path)
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def is_staff(function):
	def wrap(request,*args,**kwargs):
		if request.user.is_authenticated:
			if request.user.user_type == 2 or request.user.user_type == 1:
				return function(request,*args,**kwargs)
			else:
				messages.info(request,'Not Authorized')
				prev_url = request.META.get('HTTP_REFERER')
				cur_url = request.get_full_path()
				print(prev_url)
				if prev_url:
					redirect_url = 'homepage' if cur_url in prev_url else prev_url
				else:
					redirect_url = 'homepage'
				print(redirect_url)
				return redirect(redirect_url or 'homepage',)
		else:
			return redirect(redirect('login').url+'?next='+request.path)
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def is_student(function):
	def wrap(request,*args,**kwargs):
		if request.user.is_authenticated:
			if request.user.user_type == 3 or request.user.user_type == 1:
				return function(request,*args,**kwargs)
			else:
				messages.info(request,'Not Authorized')
				prev_url = request.META.get('HTTP_REFERER')
				cur_url = request.get_full_path()
				print(prev_url)
				if prev_url:
					redirect_url = 'homepage' if cur_url in prev_url else prev_url
				else:
					redirect_url = 'homepage'
				print(redirect_url)
				return redirect(redirect_url or 'homepage',)
		else:
			return redirect(redirect('login').url+'?next='+request.path)
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap

def event_started(function):
	def wrap(request,*args,**kwargs):
		pass
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap