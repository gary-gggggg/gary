from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html = '''<form method='get' action="/test_get">
    <p>
        姓名:<input type="text" name="uname">
    </p>
    <p>
        <input type="submit" name="提交">
    </p>
</form>'''

html2 = '''<form method='post' action="/test_post">
    <p>
        姓名:<input type="text" name="uname">
    </p>
    <p>
        <input type="submit" name="提交">
    </p>
</form>'''


def test_get(request):
    # 后端收到客户端提交的查询字符串。打印
    # 1要求查询字符串中存在名称uname的数据，如果没有，报错
    # uname=request.Get['uname']
    # 2另一种方式，试着获取，没有数据也不报错，返回值是none而已
    # 3.试着获取有值拿值，没值使用默认值
    uname = request.GET.get('uname', 'fiao')  # 后面的那个为默认值
    print(uname)
    # 4.如果有多个值，
    print(request.GET.getlist('a'))
    return HttpResponse(html)


def test_post(request):
    if request.method == 'GET':
        return HttpResponse(html2)
    elif request.method == 'POST':
        uname = request.POST['uname']
        # 与GET类似，也有
        # request.POST.get('uname',默认值)
        # request.POST.getlist(表单单元名称（如上面的‘a’）)
        return HttpResponse(f'我草你吗{uname}')


def birthday(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    return HttpResponse(f"您的生日为{year}年{month}月{day}日")


def Hello():
    return '我给你奶子一拳'


def test_html(request):
    # 返回一个模板页
    # 1.t = loader.get_template('test_html.html')
    # html3 = t.render()
    # return HttpResponse(html3)
    # 2.方法2用render直接提交，这种方式用的更加多一点
    # dict1 = {}
    # dict1['name'] = 'giao'
    # dict1['count'] = '123214'
    # dict1['city'] = ['杭州', '上海', '深圳', '广东', '成都', '重启']
    # dict1['distribute'] = {'杭州': 1325, "上海": 74565, "广东": 123473, '成都': 1231421, '重庆': 1789}
    # dict1['p1'] = Person('鲁迅', 39)
    # dict1['function1']=Hello
    # js脚本
    # dict1['script'] = '<script>alert("我日你吗")</script>'
    # return render(request, 'test_html.html', dict1)
    # 方式3:
    name = 'giao,love u'
    count = "100"
    city = ['杭州', '上海', '深圳', '广东', '成都', '重启']
    distribute = {'杭州': 1325, "上海": 74565, "广东": 123473, '成都': 1231421, '重庆': 1789}
    p1 = Person('鲁迅', 39)
    function1 = Hello
    # js脚本
    script = '<script>alert("我日你吗")</script>'
    persons = ['丁丁', 'DC', '啦啦', '波', '宝宝奶昔']
    return render(request, 'test_html.html', locals())


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def showData(self):
        return f'姓名：{self.name}，年龄：{self.age}'


def test_clac(request):
    if request.method == 'GET':
        return render(request, 'test-calc.html')
    elif request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        if not x or not y:
            return HttpResponse('请输入数据')
        # 数值判断
        try:
            x = int(x)
            y = int(y)
        except:
            return HttpResponse('请输入整数')
        result = 0
        op = request.POST['op']
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'test-calc.html', locals())
