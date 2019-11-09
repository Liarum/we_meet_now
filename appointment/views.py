from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'appointment/base.html')

def schedule(request, id):
    if request.method=='POST':
        # post 요청일 때는 파라미터로 넘어온 id==meeting 의 아이디 -> 를 참조하고 있는 user들을 찾아서 빈 시간들을 찾아준다

        pass

    else:
        # get 요청일 때는 약속시간 잡는 폼을 보내준다
        return render(request, 'appointment/input_schedule.html')