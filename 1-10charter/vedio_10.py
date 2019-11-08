from flask import Flask, views

app = Flask(__name__)
app.debug = True
app.secret_key = 'Tom123546'

'''
---------------------------------------
CBV模式，定义路由
---------------------------------------
'''


def auth(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner


class IndexView(views.MethodView):
    method = ["GET"]
    decorators = [auth, ]

    def get(self):
        return "Index.GET"

    def post(self):
        return "Index.POST"


app.add_url_rule("/index", view_func=IndexView.as_view(name="index"))  # name = endpoint
# 看源码中的 as_view() 方法

if __name__ == "__main__":
    app.run()
