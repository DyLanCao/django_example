from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.hello), 
    path('login/', views.login, name='login'),  # 这里设置name，为了在模板文件中，写name，就能找到这个路由
    path('book/', views.book, name='book'),
    path('movie/', views.movie, name='movie'),
    path('book/detail/<book_id>/<catgray>/', views.book_detail, name='detail'),]
 
