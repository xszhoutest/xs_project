from django.conf.urls import url

from userapp.views import *


urlpatterns = [
    # 声明主页面的请求
    url(r'^register', register, name='register'),
]