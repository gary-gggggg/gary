from django.http import HttpResponse


def set_cookies(request):
    resp = HttpResponse('set cookies successfully')
    resp.set_cookie('uname', 'giaoid673248932', 60)
    return resp


def get_cookies(request):
    uname = request.COOKIES.get('uname', 'default value')
    result = f'uname is {uname}'
    return HttpResponse(result)


def del_cookies(request):
    resp = HttpResponse('delete cookies successfully')
    resp.delete_cookie('uname')
    return resp


def set_session(request):
    request.session['uname'] = 'giao'
    return HttpResponse('set session successfully')


def get_session(request):
    uname1 = request.session.get('uname', 'default value')
    result = f'uname is {uname1}'
    return HttpResponse(result)


def del_session(request):
    if 'uname' in request.session:
        del request.session['uname']
    return HttpResponse('delete session successfully')
