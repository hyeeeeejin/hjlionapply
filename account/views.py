from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm # 장고에서 제공하는 로그인, 회원가입 폼
from django.contrib.auth import login, logout
from .forms import RegisterForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        regist_form = RegisterForm(request.POST)
        if regist_form.is_valid():
            regist_user = regist_form.save()
            login(request, regist_user)
            return redirect('urlhome')
        else:
            form = RegisterForm()
            return render(request, 'signup.html', {'registerform': form})
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'registerform': form})

def login_view(request):
    if request.method == 'POST':  # 폼에서 post 방식으로 받을 때
        auth_form = AuthenticationForm(request=request, data = request.POST)  # 저 초록색 f12 눌러바.
        if auth_form.is_valid():  # auth_form을 장고에서 제공한 is_valid 함수를 통해 유효성 검사를 받음.
            auth_username = auth_form.cleaned_data.get('username')
            auth_password = auth_form.cleaned_data.get('password')
            auth_user = authenticate(request=request, username = auth_username, password = auth_password)
            login(request, auth_user)
            return redirect('urlhome')
        else: return redirect('urllogin')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'login_form':form})

def logout_view(request):
    logout(request)
    return redirect('urlhome')