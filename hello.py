from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/user/<int:id>')
def user_id(id):
    return '<h1>Hello, user your id is %s!</h1>' % id


if __name__ == '__main__':
    app.run(debug=True)
