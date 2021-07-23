from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:   # 설명표, 꼬리표 같은 것. 
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'name', 'major', 'student_id']
