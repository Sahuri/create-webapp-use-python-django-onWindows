## Create models

We will create a news content on main page at our website.   

1. Go to on Command Prompt type _cd Django01_
2. Activate virtual environment with type _myvenv\Scripts\activate_
3. Type _python manage.py startapp blog_
4. Register site on Setting.py file in \Django01\mysite with add script :
```python
INSTALLED_APPS = [
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
     'blog'
 	]	
```
6. Open models.py file in folder \Django01\blog.
7. Add the following script :
```python
 from django.db import models
 from django.utils import timezone

 class News(models.Model):
 	  author = models.ForeignKey('auth.User')
 	  title = models.CharField(max_length=200)
 	  image=models.CharField(max_length=200)
 	  text = models.TextField()
 	  created_date = models.DateTimeField(default=timezone.now)
 	  published_date = models.DateTimeField(blank=True, null=True)

 	def publish(self):
 		  self.published_date = timezone.now()
 		  self.save()
 
 	def __str__(self):
 		  return self.title
``` 
8. Type _python manage.py makemigrations blog_
9. Type _python manage.py migrate blog_
