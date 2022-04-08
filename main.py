from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    return '<h1>Hi, %s!</h1>' % name


if __name__ == '__main__':
    app.run()