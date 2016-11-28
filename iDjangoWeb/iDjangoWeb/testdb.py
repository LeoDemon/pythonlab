# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import book_info
from TestModel.models import user_info
import datetime

#book_info
def testMysql(request):
    #insert data
    testsql1 = book_info(book_id=10001, book_name='Python基础教程', book_purchase_time=datetime.date(2016,11,22))
    testsql2 = book_info(book_id=10002, book_name='GitHub入门与实践', book_purchase_time=datetime.date(2016,11,23))
    testsql3 = book_info(book_id=10003, book_name='鸟哥的linux私房菜', book_purchase_time=datetime.date(2016,11,23))
    testsql1.save()
    testsql2.save()
    testsql3.save()
    response_str = '<h2>恭喜，[book_info] records have been saved to Mysql DataBase!</h2>'

    #display list
    response_str +='<div><h3>After insert, the book list is:</h3>'
    record_list = book_info.objects.all()
    display_str = testDisplay(record_list)
    response_str += display_str
    response_str += '</div>'

    #update record
    response_str +='<br/><div><h3>After update, the book list is:</h3>'
    book_info.objects.filter(book_id=10001).update(book_name='Python核心编程第三版')
    book_info.objects.filter(book_id=10002).update(book_purchase_time=datetime.date(2016,11,8))
    record_list = book_info.objects.all()
    display_str = testDisplay(record_list)
    response_str += display_str
    response_str += '</div>'

    #delete record
    response_str +='<br/><div><h3>After delete, the book list is:</h3>'
    del_book = book_info.objects.get(book_id=10003)
    del_book.delete()
    record_list = book_info.objects.all()
    display_str = testDisplay(record_list)
    response_str += display_str
    response_str += '</div>'

    return HttpResponse(response_str)

def testDisplay(record_list):
    # display_str = '<table border=1 cellpadding=10>'
    # display_str += '<tr align=center><td>book_id</td><td>book_name</td><td>book_purchase_time</td></tr>'
    # for record in record_list:
        # display_str += '<tr align=center>'
        # display_str += '<td>'+str(record.book_id)+'</td>';
        # display_str += '<td>'+record.book_name.encode('utf-8')+'</td>';
        # display_str += '<td>'+str(record.book_purchase_time)+'</td>';
        # display_str += '</tr>'

    display_str = '|---book_id---|---book_name---|---book_purchase_time---|</br>'
    for record in record_list:
        display_str += '|---'+str(record.book_id);
        display_str += '---|---'
        display_str += record.book_name.encode('utf-8');
        display_str += '---|---'
        display_str += str(record.book_purchase_time);
        display_str += '---|'
        display_str += '<br/>'

    return display_str;


#user_info
def ChkWmnLogin(reqinfo):
    username = reqinfo['name']
    password = reqinfo['password']
    recout = {'ErrCode':'0', 'ErrMsg':''}

    # no record should use filter function,
    # otherwise there will raise Exception "DoesNotExist: user_info matching query does not exist."
    # qry_user = user_info.objects.get(user_name=username)
    qry_user = user_info.objects.filter(user_name=username)
    if qry_user:
        curr_user_info = qry_user[0]
        recout['alias_name'] = curr_user_info.user_alias
        if(curr_user_info.user_pwd== password):
            pass
        else:
            recout['ErrCode'] = '10005'
            recout['ErrMsg'] = 'sorry，密码不正确，请确认!'

    else:
        recout['ErrCode'] = '10004'
        recout['ErrMsg'] = '无此用户，请确认!'
        print("---no user_info---")

    return recout

