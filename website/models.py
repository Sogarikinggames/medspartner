from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('お名前', validators=[DataRequired()],render_kw={'placeholder': '山田太郎'})
    email = StringField('メールアドレス', validators=[DataRequired(), Email()],render_kw={'placeholder': 'example@mail.com'})
    message = TextAreaField('お問い合わせ内容の詳細', validators=[DataRequired()],render_kw={'placeholder': 'お問い合わせ内容を入力してください'})
    submit = SubmitField('今すぐ問い合わせする')