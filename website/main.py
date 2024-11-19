from flask import Blueprint, render_template, request, redirect, flash,url_for
from flask_mail import Message
from .models import ContactForm
from . import mail

main = Blueprint('main', __name__)

# home
@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html')


#aboutme
@main.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

#contact
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message('Contact Form Message',
                      sender=form.email.data,
                      recipients=['sogari812@gmail.com'])  # 固定送信先
        msg.body = f"""
        From: {form.name.data} <{form.email.data}>
        Message: {form.message.data}
        """
        mail.send(msg)
        return redirect('/contact')
    return render_template('contact.html', form=form)