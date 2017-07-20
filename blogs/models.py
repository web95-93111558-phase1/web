from django.db import models
from users.models import MyUser
from django.utils import timezone

class BlogManager(models.Manager):
	def create_Blog(self,user):
		blog = self.create(user=user)
		return blog

class Blog(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	objects = BlogManager()
	def __str__(self):
		return "id : "+str(self.pk)
	
class PostManager(models.Manager):
	def create_Post(self,blog,input):
		post = self.create(blog=blog,title=input['title'],summary=input['summary'],text=input['text'])
		return post
	
	
class Post(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	summary = models.TextField()
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now())
	objects = PostManager()
	def as_dict(self):
		return {
			'id':self.id,
            'title': self.title,
            'summary' : self.summary,
			'datetime': self.date
        }
		
	def as_dict2(self):
		return {
            'title': self.title,
            'summary' : self.summary,
			'text': self.text,
			'datetime': self.date
        }
		
	def __str__(self):
		return "id : "+str(self.pk)
class CommentManager(models.Manager):
	def create_Comment(self,post,input):
		comment = self.create(post=post,text=input['text'])
		return comment 
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.TextField()
	objects = CommentManager()
	date = models.DateTimeField(default=timezone.now())
	
	def __str__(self):
		return "id : "+str(self.pk)
	
	def as_dict(self):
		return {
            'text': self.text,
			'datetime': self.date
        }