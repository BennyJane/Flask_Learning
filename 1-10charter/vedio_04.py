def wrapper(func):
    def inner(*args, **kwargs):
        print('inner is running!')
        return func(*args, **kwargs)

    print("return is now!")
    return inner


# 执行顺序， wrapper() --> return inner --> def inner():
@wrapper
def index(num):
    print("index is running!")
    return num


# 返回值为 NoneType
res = index(100)
print(type(res), res)
print(
    '''
    ---------------------------------------
    next is 2 example！
    ---------------------------------------
    ''')


def wrapperTwo(options):
    def inner(func, *args, **kwargs):
        print('inner is running!')
        print(type(func))
        return func(*args, **kwargs)

    print("index is running!")
    return inner


# 执行顺序 inner = wrapperTwo() --> @inner 被装饰函数传入执行--> inner(indexTwo)
# TODO 直接被执行了，不需要调用
@wrapperTwo({'key': '152'})
def indexTwo(res=15):
    print(res)
    pass


print(
    '''
    ---------------------------------------
    next is 3 example！
    ---------------------------------------
    ''')

# 利用装饰器， 直接添加路由
url_map = {

}


def route(option):
    def inner(func, *args, **kwargs):
        url_map[option["path"]] = func

    return inner


@route({"path": "/index"})
def index(request):
    pass


print(url_map)

'''
---------------------------------------
session & cookie 的原理
---------------------------------------
'''

'''
---------------------------------------
自定义字典
---------------------------------------
'''


class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super(MyDict, self).__init__(*args, **kwargs)
        self['name'] = 'benny'
        self['modify'] = True


'''
---------------------------------------
Django: 重武器， 包含非常多组件， ORM Form ModelForm 缓存 Session 中间件 信号等
Flask: 短小精悍，内部组件少， 但第三方组件非常丰富； 小项目更快速，但也可以胜任大项目

* Tornado: 异步非阻塞框架（node.js）， 通过一个线程执行1000个任务

bottle：更小
web.py： 老
等
---------------------------------------
'''

'''
---------------------------------------
安装：
* wsgi， werkzeug
---------------------------------------
'''
