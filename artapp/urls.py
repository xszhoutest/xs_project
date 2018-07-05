from django.conf.urls import url
<<<<<<< HEAD

from artapp import views_art
from artapp.views import *

=======
from artapp.views import *


>>>>>>> 5559f1ad351c66c9647e666c9a00fdf7b51ce695
urlpatterns = [
    # 声明主页面的请求
    url(r'^tags', add_tags),
    url(r'^list_tags', list_tags),
    url(r'^delete_tag', delete_tag),
<<<<<<< HEAD
    url(r'^art_edit$', views_art.art_edit),
    url(r'^search', views_art.search),  # 搜索文章
    url('^$', index),
=======
    url(r'^add_novel', add_novel),
    url('^', index),
>>>>>>> 5559f1ad351c66c9647e666c9a00fdf7b51ce695
]