from django.shortcuts import render, redirect
from userapp.models import UserProfile

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'user/register.html')

    else:
        user = UserProfile()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.phone = request.POST.get('phone')
        user.icon = request.FILES.get('icon')

        # 保存前要验证
        user.save()
        return redirect('art/')
