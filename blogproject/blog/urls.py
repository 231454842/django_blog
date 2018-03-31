from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index,name='index'),
    re_path('post/(?P<pk>[0-9]?)/',views.detail,name='detail'),
    #re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/',views.archives,name='archives')
    re_path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/',views.archives,name='archives'),
    re_path('categary/(?P<pk>[0-9]+)/',views.categary,name='categary')
]
