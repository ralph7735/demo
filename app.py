from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)

def datetime_format(value,format="%Y-%d-%m %H:%M"):
    return value.strftime(format)

app.add_template_filter(datetime_format,"dformat")

class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email

@app.route("/")
def hello_world():
    user=User(username="zhiliao",email="xx@qq.com")
    person = {
        "username":"zhangsan",
        "email":"zhangsan@qq.com"
    }


    return render_template("index.html",user=user,person=person)

@app.route("/blog/<blog_id>")
def blog_detail(blog_id):

    return render_template("blog_detail.html",blog_id=blog_id,username="zhiliao")

@app.route("/filter")
def filter_demo():
    user=User(username="zhilixx",email="sdf@qq.com")
    mytime=datetime.now()

    return render_template("filter.html",user=user,mytime=mytime)

@app.route("/control")
def control_statement():
    age=17
    books=[
        {"name":"sanguoyanyi",
         "author":"luoguanzhong"

        },
        {
            "name":"shuihuzhuan",
            "author":"shinaian"
        }
    ]
    return render_template("control.html",age=age,books=books)

@app.route("/child1")
def child1():
    return render_template("child1.html")

@app.route("/child2")
def child2():
    return render_template("child2.html")

@app.route("/static")
def static_demo():
    return render_template("static.html")



if __name__=="__main__":
    app.run(debug=True)