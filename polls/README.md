from polls.urls import urlpatternsfrom django.conf.urls.i18n import urlpatterns

## 📁 Django 应用说明

应用是一个专门做某件事的网络应用程序--比如博客系统，或者公共记录的数据库，或者小型的投票程序。  
项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

---


### 创建一个应用

`python manage.py startapp polls` 这将创建一个名为 polls 的目录，其布局如下：
```
polls/
|-- __init__.py
|-- admin.py
|-- apps.py
|-- migrations/
|   |-- __init__.py
|-- models.py
|-- tests.py
|-- urls.py
└── views.py
```

---

### 编写视图

#### 🐍 Python: polls/views.py
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

要在浏览器中访问，需要将其映射到一个 URL，因此需要定义一个 URL 配置，简称 “URLconf”。这些 URL 配置是在每个 Django 应用程序内部定义的，它们名为 urls.py。  
要为 polls 应用定义一个 URLconf，创建一个名为 polls/urls.py 的文件，并包含以下内容
#### 🐍 Python: polls/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

---
### 配置项目中的 根URLconf
要在根 URLconf 中添加应用的 URLconf，需要在项目的 urls.py 中导入 `django.urls.include`,   
并在 `urlpatterns` 列表中插入一个 `include()`,如下：
#### mysite/urls.py
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.url")),
    path("admin/", admin.site.urls)
]
## path() 函数至少需要两个参数: route 和 view（视图）。
## 每当 Django 遇到 include() 时，它会截断 URL中匹配到该点的部分，并将剩余的字符串发送到包含的 URLconf 以进行进一步处理。
```