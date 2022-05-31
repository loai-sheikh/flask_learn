from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Hello', sender='sender@gmail.com', recipients=['reciver@gmail.com'])
    msg.body = "Hello Flask! this message is sent from Flask-Mail"
    mail.send(msg)
    return "Message send"


if __name__ == '__main__':
    app.run(debug=True)
