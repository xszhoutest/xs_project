from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')

    # django 的密码生成器生成   make_password
    password = models.CharField(max_length=100, verbose_name='密码')

    phone = models.CharField(max_length=13, verbose_name='电话')

    # upload_to 指定的是相对于settings中设置的MEDIA_ROOT的路径
    icon = models.ImageField(upload_to='users', verbose_name='头像')

    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    # 最后登录时间
    login_time = models.DateTimeField(auto_now=True, verbose_name='最后登录时间')

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户信息'



