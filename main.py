#Import modules
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from flask_mail import Mail,Message
from config import mail_username,mail_password


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_SENDER'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

ckeditor = CKEditor(app)
Bootstrap(app)
mail = Mail(app)

#Contact page
@app.route('/',methods=["GET","POST"])
def contact():
    if request.method =="POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        msg = Message(subject=f"Mail from {name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n{message}",sender=mail_username,recipients=['munasinghehiruka@gmail.com'])
        mail.send(msg)
        return render_template("index.html",success=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)