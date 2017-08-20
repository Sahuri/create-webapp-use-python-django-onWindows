## Add html template and config urls

1. Go to on Command Prompt type _cd Django01_.
2. Create \Django01\blog\templates\blog folder.
3. Create news_file.html in it, the following script :
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>My Blog</title>
    </head>
    <body>
        {{news}}
    </body>
</html>
```
4. Open views.py file in \Django01\blog folder then edit the following script :
```python
from django.shortcuts import render
from django.utils import timezone
from .models import News

def post_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/news_list.html', {'news': news})
```
5. Create urls.py file in \Django01\blog folder then add the following script :
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
]
```
6. Open urls.py in \Django01\mysite edit the following script :
```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
```
7. Activate virtual environment with type _myvenv\Scripts\activate_.
8. Run your webapp with type _python manage.py runserver
9. Open browser type _localhost:8000_ on url.