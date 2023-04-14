from flask import Flask, request, make_response, abort

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    message = '<p>Your browser is %s</p>' % user_agent

    response = make_response(message)
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/user/<int:id>')
def user_id(id):
    return '<h1>Hello, user your id is %s!</h1>' % id


if __name__ == '__main__':
    app.run(debug=True)
