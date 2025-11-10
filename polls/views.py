from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
这是在 Django 中最基本的视图，要在浏览器访问，需要将其映射到一个 URL 。
故应该定义一个 URL 配置，简称为“URLconf”。
这些 URL 配置是在每个 Django 应用程序内部定义的，它们是名为 urls.py 的 python 文件。
"""

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
