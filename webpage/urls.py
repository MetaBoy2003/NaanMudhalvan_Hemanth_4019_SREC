from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blog, name='blog'),
     path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('upload/', views.upload, name='upload'),
]
