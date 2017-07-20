from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Blog,Post,Comment
from .forms import PostForm,CommentForm,SearchForm
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.http import HttpResponseRedirect


def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})



@csrf_exempt
def posts(request):
	if request.method == 'GET':
		c =Blog.objects.filter(id = request.GET['blog']).exists()
		if c :
			posts = Post.objects.filter(blog_id = request.GET['blog'])
			if 'offset' in request.GET:
				offset = int(request.GET['offset'])
				posts = posts[offset:]
			if 'count' in request.GET:
				count = int(request.GET['count'])
				posts = posts[:count]
			dictionaries = [obj.as_dict() for obj in posts]
			return JsonResponse({
				'status': 0,
				'posts': dictionaries
			})
		else:
			return JsonResponse({
                'status': -1,
                'posts': 'not found'
            })
		
@csrf_exempt
def post(request):
	if request.method == 'GET':
		if Post.objects.filter(blog_id = request.GET['blog'] , id = request.GET['id']).exists():
			post = Post.objects.get(blog_id = request.GET['blog'] , id = request.GET['id'])
			return JsonResponse({
				'status': 0,
				'post': post.as_dict2()
			})
		else:
			return JsonResponse({
				'status': -1,
				'post': 'not found'
			})		
	if request.method == 'POST':
		c = Blog.objects.filter(id = request.POST['blog']).exists()
		if c :
			blog = Blog.objects.get(id = request.POST['blog'])
			token = request.META.__getitem__('HTTP_X_TOKEN')
			c = default_token_generator.check_token(blog.user, token)
			if	c : 
				form = PostForm(request.POST)
				if form.is_valid():
					blog = Blog.objects.get(id = request.POST['blog'])
					post = Post.objects.create_Post(blog,request.POST)
					return JsonResponse({
						'status': 0,
						'post_id': post.id
					})
				else :
					message = form.errors
					m = ''
					for e in message.values():
						m+=e
					return JsonResponse({
						'status': -1,
						'massage': m
					})
			else:
				return JsonResponse({
					'status': -1,
					'posts': 'token is invalid'
				})			
		else:
			return JsonResponse({
				'status': -1,
				'posts': 'blog not found'
			})		
			
			

@csrf_exempt
def comments(request):
	if request.method == 'GET':
		c = Post.objects.filter(id = request.GET['post_id']).exists()
		if c:
			comments = Comment.objects.filter(post_id = request.GET['post_id'])
			if 'offset' in request.GET:
				offset = int(request.GET['offset'])
				comments = comments[offset:]
			if 'count' in request.GET:
				count = int(request.GET['count'])
				comments = comments[:count]
			dictionaries = [obj.as_dict() for obj in comments]
			return JsonResponse({
				'status': 0,
				'comments': dictionaries
			})
		else :
			return JsonResponse({
				'status': -1,
				'comments': 'not found'
			})

@csrf_exempt
def comment(request):
	if request.method == 'POST':
		c = Post.objects.filter(id = request.POST['post_id']).exists()
		if c :
			form = CommentForm(request.POST)
			if form.is_valid():
				post = Post.objects.get(id = request.POST['post_id'])
				comment = Comment.objects.create_Comment(post,request.POST)
				return JsonResponse({
					'status': 0,
					'comment_id': comment.id
				})
			else :
				return JsonResponse({
					'status': -1,
					'massage': 'input is not valid'
				})
		else :
			return JsonResponse({
				'status': -1,
				'massage': 'post not found'
			})