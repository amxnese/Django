"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='blog-register')
]

'''
In Django, the urlpatterns variable in a project's urls.py file defines the mapping between
URLs and views. The include() function is used to include patterns from other URLconfs.

path('blog/', ...) specifies a URL pattern that matches any URL starting with "blog/".
include('blog.urls') tells Django to include the URLs defined in another URLconf file located at 'blog.urls'.
So, when a user visits a URL that starts with "blog/", Django will look for further URL patterns 
(patterns that comes after the blog/ , meaning if the url is blog/about, django will only look for 
a url that mathches about in the blog.urls, so if we pass only blog/, django will look for a url 
that matches an empty string) in the blog.urls module and match them accordingly. This helps in 
organizing URLs into smaller, modular components, 
making the codebase more maintainable and easier to manage.
'''