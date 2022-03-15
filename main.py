from flask import Flask, render_template,request,redirect
from models import db,Todo
from flask_mail import Mail, Message
import smtplib

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'prashanthsonu94@gmail.com'
app.config['MAIL_PASSWORD'] = 'xxxxxxxxx'
mail = Mail(app)

@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/data/create',methods=['GET','POST'])
def main_page():
    if request.method=='GET':
        return render_template('home.html')
    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        image=request.files('image')
        todo=Todo(title=title ,description=description,image=image)
        db.session.add(todo)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def RetrieveList():
    alltodos=Todo.query.all()
    return render_template('datalist.html',todos=alltodos)
 
@app.route('/data/<int:sno>')
def Retrieve_todo(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    if todo:
        return render_template('data.html',todo=todo)
    return "todo with {} Does not exist".format(sno)


# @app.route("/send_email",methods=["GET","POST"])
# def send_email():
#     try:
#         msg = Message('Hello from the other side!', sender = "prashanthsonu94@gmail.com", recipients = ["prashanthsonu94@gmail.com"])
#         msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
#         mail.send(msg)
#         return "Message sent!"
#     except Exception as e:
#         raise e


import smtplib
import socket
from smtplib import SMTPException


s = socket.socket()

sender = 'prashanthsonu94@gmail.com'
receivers = ['prashanthsonu94@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

@app.route("/send_email",methods=["GET"])
def send_email():
    try:
        smtpObj = smtplib.SMTP('localhost')
        s=smtpObj.sendmail(sender, receivers, message) 
        cs.send(s)
        cs.close()        
        print("Successfully sent email")
    except SMTPException:
        raise e
        print("?????????????")



if __name__ == "__main__":
    app.run(debug=True,port=8000)