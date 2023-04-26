from flask_mail import Message
from hello import app, mail

app_ctx = app.app_context()
app_ctx.push()

msg = Message('test subject', sender='me@example.com',
              recipients=['me@examle.com'])
msg.body = 'test body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)