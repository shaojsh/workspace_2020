from django.conf.urls import url

from .views import *

urlpatterns = [
    # 配置多级路由
    #设置默认页
    url(r'^$', index),
    # url(r'^reg$', reg),
    url(r'^index', index),
    url(r'^blogDel-kugou', blogPostKogou),
    url('ajax_song/', ajax_song),
    url(r'^blog-post', blogPost),
    url(r'^uploadFiles', uploadFiles),
    url(r'^delete_class', delete_class),
    url(r'^downloadFiles', downloadFiles),
    url(r'^about', aboutme),
    url(r'^searchBlogPost', searchBlogPost),
]