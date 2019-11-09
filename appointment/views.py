from django.shortcuts import render, redirect
from . import models

from .models import Meeting, User

# Create your views here.


def test(request):
    ret_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[],
                11:[], 12:[], 13:[], 14:[], 15:[]}

    tmp = [[4, 3, 8, 8, 7, 5, 7, 8, 5, 4, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 3, 1, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0
, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 2, 4, 2, 3, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0
, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]]

    for i in range(16):
        for j in range(7):
            ret_dict[i].append(tmp[j][i])

    print(ret_dict[0])

    return render(request, 'appointment/show_result.html', {
        'a': ret_dict[0],
        'b': ret_dict[1],
        'c': ret_dict[2],
        'd': ret_dict[3],
        'e': ret_dict[4],
        'f': ret_dict[5],
        'g': ret_dict[6],
        'h': ret_dict[7],
        'i': ret_dict[8],
        'j': ret_dict[9],
        'k': ret_dict[10],
        'l': ret_dict[11],
        'm': ret_dict[12],
        'n': ret_dict[13],
        'o': ret_dict[14],
        'p': ret_dict[15],
    })


def index(request):
    return render(request, 'appointment/homepage.html')


def meeting(request):
    if request.method == 'POST':
        meeting = Meeting()
        meeting.name = request.POST["meeting_name"]
        meeting.save()


        return redirect('schedule', id=meeting.id)

def schedule(request, id):
    if request.method=='POST':
        user = User()
        meeting = Meeting.objects.get(id=id)
        user.meeting = meeting
        user.name = request.POST["user_name"]
        dates = ['0[]', '1[]', '2[]', '3[]', '4[]', '5[]', '6[]']

        for i in range(7):
            schedule = request.POST.getlist(dates[i])
            string_schedule = ""
            for j in schedule:
                string_schedule = string_schedule + j + " "  # 1 2 3 4 5 이런식으로 string 저장
                print(string_schedule)

            if i==0:
                user.mon = string_schedule
            elif i==1:
                user.tue = string_schedule
            elif i==2:
                user.wed = string_schedule
            elif i==3:
                user.thr = string_schedule
            elif i==4:
                user.fri = string_schedule
            elif i==5:
                user.sat = string_schedule
            else:
                user.sun = string_schedule

        user.save()

        res = searching(meeting)
        print(res)

        return render(request, 'appointment/show_result.html', {
            'id': id
        })
        # post 요청일 때는 파라미터로 넘어온 id==meeting 의 아이디 -> 를 참조하고 있는 user들을 찾아서 빈 시간들을 찾아준다

        # meeting = Meeting.objects.get(id=id)
        # users = meeting.user_set.all()
        # users = User.objects.get(meeting=meeting)
        print("request ok")
        print(request.POST['user_name'])
        # for i in range(7):
        #     print(request.POST.getlist(str(i)))
        print(request.POST.getlist('1[]'))

        return render(request, 'appointment/input_schedule.html', {
            'id': id
        })

    else:
        # get 요청일 때는 약속시간 잡는 폼을 보내준다, id도 같이 넘겨줘야 함
        return render(request, 'appointment/input_schedule.html', {
            'id': id
        })

def searching(meeting):
    monday=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    tuesday=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    wednesday=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    thursday=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    friday=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    saturday=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sunday=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lst=[monday,tuesday,wednesday,thursday,friday,saturday,sunday]
    users = meeting.user_set.all()
    print(users)
    for i in range(len(users)):
        users[i].mon=list(map(int,users[i].mon.split()))
        users[i].tue=list(map(int,users[i].tue.split()))
        users[i].wed=list(map(int,users[i].wed.split()))
        users[i].thr=list(map(int,users[i].thr.split()))
        users[i].fri=list(map(int,users[i].fri.split()))
        users[i].sat=list(map(int,users[i].sat.split()))
        users[i].sun=list(map(int,users[i].sun.split()))
        for a in range(len(users[i].mon)):
            monday[users[i].mon[a]-8]+=1
        for a in range(len(users[i].tue)):
            tuesday[users[i].tue[a]-8]+=1
        for a in range(len(users[i].wed)):
            wednesday[users[i].wed[a]-8]+=1
        for a in range(len(users[i].thr)):
            thursday[users[i].thr[a]-8]+=1
        for a in range(len(users[i].fri)):
            friday[users[i].fri[a]-8]+=1
        for a in range(len(users[i].sat)):
            saturday[users[i].sat[a]-8]+=1
        for a in range(len(users[i].sun)):
            sunday[users[i].sun[a]-8]+=1
    return lst