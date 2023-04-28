#! -*- coding:utf-8 -*-


from flask import Flask, request, render_template


app = Flask(__name__)


# ok
@app.route("/")
def homepage():
    return render_template("index.html")


# 路由管理
if __name__ == '__main__':
    app.run(debug=True, port=8888)
