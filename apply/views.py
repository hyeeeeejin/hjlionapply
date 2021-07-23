from django.shortcuts import render, get_object_or_404, redirect
from .models import Apply
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def home(request) :
    allblogs = Apply.objects.all()
    c = allblogs.count()
    return render(request, 'home.html', {'ablog':allblogs, 'count':c} )

def detail(request, id):
    oneblog = get_object_or_404(Apply, pk = id)
    return render(request, 'detail.html', {'o' : oneblog})

def new(request):
    return render(request, 'new.html')

def create(request):
    if Apply.objects.filter(snum = request.POST['csnum']).exists():
        eapply = get_object_or_404(Apply, snum = request.POST['csnum'])
        messages.info(request, '한 계정당 하나의 지원서만 작성 가능합니다!')
        return redirect('urldetail', eapply.id)
    cblog = Apply()
    cblog.name = request.POST['cname']  # home.html의 name부분과 같음.(저 주황색)
    cblog.snum = request.POST['csnum']
    cblog.dept = request.POST['cdept']
    cblog.motive = request.POST['cmotive']
    cblog.service = request.POST['cservice']
    cblog.saw = request.POST['csaw']
    cblog.aspire = request.POST['caspire']
    cblog.time = timezone.now()
    cblog.image = request.FILES.get('cimage')
    cblog.save()                           # 넘겨받은 것을 저장
    return redirect('urldetail', cblog.id)  # redirect는 요청을 url로 넘겨주는 용도. cblog.id가 붙는 이유는 번호가 붙어서 불러온느 것이기 떄문.

def edit(request, id):  # 작성한 내용이 불러져 와야 하기 때문에 id 추가함.
    eblog = Apply.objects.get(id = id)  # 두 번째 id는 위 detail에서 받은 pk = id 부분을 말함. 모델의 객체에서 get방식으로 받아오겠다.
    return render(request, 'edit.html', {'e':eblog})

def update(request, id):
    ublog = Apply.objects.get(id = id)
    ublog.name = request.POST['uname']
    ublog.snum = request.POST['usnum']
    ublog.dept = request.POST['udept']
    ublog.motive = request.POST['umotive']
    ublog.service = request.POST['uservice']
    ublog.saw = request.POST['usaw']
    ublog.aspire = request.POST['uaspire']
    ublog.time = timezone.now()
    ublog.image = request.FILES.get('uimage')
    ublog.save()
    return redirect('urldetail', ublog.id)

def delete(request, id):
    dblog = Apply.objects.get(id = id)
    dblog.delete()
    return redirect('urlhome')