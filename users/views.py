from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import UserForm
from .models import MyUser
from blogs.models import Blog
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate

@csrf_exempt
def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = MyUser.objects.create_MyUser(request.POST)
			user.set_password(request.POST['password'])
			user.save()
			blog = Blog.objects.create_Blog(user)
			user.defaultBlog = blog.pk
			user.save()
			return JsonResponse({
				'status': 0,
				'message': 'You have successfully registered'
			})
			#a.AddHeader("Access-Control-Allow-Origin", "*")
			#return a
		else:
			message = form.errors
			m = ''
			for e in message.values():
				m+=e
			return JsonResponse({
				'status': -1,
				'message': m
			})
@csrf_exempt
def login(request):
	user = authenticate(username=request.POST['user_name'], password=request.POST['password'])
	if user is not None:
		token = default_token_generator.make_token(user)
		return JsonResponse({
			'status': 0,
			'blog' : user.defaultBlog,
			'token' : token,
			'message' : 'You have successfully logged in'
		})
	else:
		return JsonResponse({
			'status': -1,
			'message': 'user not found',
		})

		
