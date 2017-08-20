from django.shortcuts import render
from django.utils import timezone
from .models import News

def news_list(request):
    news = News.objects.all()
    return render(request, 'blog/news_list.html', {'news': news})
