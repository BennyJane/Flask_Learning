from flask import Flask, views
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.debug = True
app.secret_key = 'Tom123546'
# app.config["SERVER_NAME"] = "oldboy.com"


# 重定向： js html中的meta
@app.route('/index', methods=["GET", "POST"], endpoint="n1", redirect_to="n2")
def index():
    return "公司老首页"


@app.route("/index2", methods=["GET", "POST"], endpoint="n2")
def index():
    return "公司新首页"


'''
---------------------------------------
app.route()的参数：

* 子域名
subdomain = None
---------------------------------------
'''

'''
---------------------------------------
app.route()的参数：
@app.route('/user/<username>')
@app.route('/post/<int:post_id>')
@app.route('/post/<float:post_id>')
@app.route('/post/<path:path>')
@app.route('/login/methods=["GET", "POST"]')

* 常用路由系统只有以上5种， 所有路由系统都是基于一种对应关系来处理的：
DEFAULT_CONVERTERS = {
    "default": UnicodeConverter,
    "string": UnicodeConverter,
    "any": AnyConverter,
    "path": PathConverter,
    "int": IntConverter,
    "float": FloatConverter,
    "uuid": UUIDConverter,
}

* 添加正则表达式路由系统
转换器转换器，是对url中的内容进行匹配和转换！
换器中的内容包括三个：路由匹配的正则regex属性，to_python方法，to_url方法。 regex是对url进行路由匹配，to_python和to_url两个方法是对url参数进行处理的。其中to_url(self, value)方法是当使用uro_for()方法指定参数时，对参数进行处理后再进行路由匹配！

1、regex：匹配url参数的正则表达式
可以通过__init__方法初始化

下面这两个方法都是对url参数进行处理，一个是在调用视图函数之前执行，一个是在路由之前执行：
2、to_python(self, value)方法
当匹配到参数后将自动调用to_python方法将参数进行处理后，在调用视图函数将参数传回给视图函数

3、to_url(self, url)方法
使用url_for()方法的时候，先调用to_url对传入的url参数进行处理，处理完成后再进行路由
---------------------------------------
'''


# 第一步： 写类
class RegexConverter(BaseConverter):
    '''
    自定义URL正则表达式
    '''

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        '''
        路由匹配时， 匹配成功后传递给视图函数种参数的值， 可在这里进行二次加工
        :param value:
        :return:
        '''
        return value

    def to_url(self, value):
        '''
        使用url_for() 反向生成URL时， 传递的参数经过该方法处理， 返回的值用于生成URL中的参数
        :param value:
        :return:
        '''
        val = super(RegexConverter, self).to_url(value)
        return val


# 2， 添加到flask中
app.url_map.converters['regex'] = RegexConverter

# ”\d+“ 被当作第二个参数传递进来 ？？
@app.route('/home/<regex("\d+"):nid>')
def home(nid):
    return "home page"


if __name__ == "__main__":
    app.run()
