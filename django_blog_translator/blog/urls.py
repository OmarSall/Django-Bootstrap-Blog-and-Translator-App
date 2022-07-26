from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name = 'blog_view'),   #when U find slug execute class BlogView as view, list of calls
    path('about/' , views.AboutView.as_view(), name = 'about_view'),
    path('', views.PostList.as_view(), name = 'home')
]