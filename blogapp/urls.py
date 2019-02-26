from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.blog, name="blog"),
  path('<int:blog_id>', views.detail, name="detail"),
  path('new/', views.new, name="new"),
  path('create/', views.create, name="create"),
  # path('newblog/', views.blogpost, name="newblog"),
  #path('account/', include('allauth.urls'))
]

