from django.conf.urls import url

from .views import *

urlpatterns = [
    # 配置多级路由
    # url(r'^reg$', reg),
    url(r'^index', index),
    url(r'^blogDel-kugou', blogPostKogou),
    url(r'^test', searchSong),
]