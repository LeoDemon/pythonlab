#-*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.shortcuts import render
from testdb import ChkWmnLogin


def hello(request):
    context = {}
    context['hello'] = "你好，Welcome to Django Web Framework!"
    context['dbcontent'] = "dbcontent!"
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello 中国 ")


def wmn_index(request):
    context = {}
    context['hello'] = "Hello, This is Working Management System, please login!"
    context['check_msg'] = ""
    return render(request, 'wmn_login.html', context)


def wmn_login(request):
    print('request==[%s]'%request.COOKIES)
    context = {}
    checkFlag = 0;
    context['check_msg'] = ""
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if("" == name):
            context['check_msg'] = "sorry, 登陆账号为空！"
        elif("" == password):
            context['check_msg'] = "sorry, 密码为空！"
        else:
            qryInput={'name':name, 'password':password}
            output = ChkWmnLogin(qryInput)
            if '0' == output['ErrCode']:
                checkFlag = 1;
                context['user_name'] = output['alias_name']
            else:
                context['check_msg'] = output['ErrMsg']
    else:
        checkFlag = 0;
        print("---post is null---")

    if 0 == checkFlag:
        repost_file =  'wmn_login.html'
    else:
        repost_file =  'wmn_main.html'

    return render(request, repost_file, context)

