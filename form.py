from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send-email', methods=['POST'])
def send_email():
    email = request.form['email']
    message = request.form['message']

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = 'New Contact Form Submission'
    msg['From'] = email
    msg['To'] = 'pythondevsvjat@gmail.com'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('pythondevsvjat@gmail.com', 'bmwavt323')
        smtp.send_message(msg)

    return 'Email sent!'

if __name__ == '__main__':
    app.run(port=8080, debug=True)