import DECRYPTOR as E
from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField,PasswordField,StringField, TextAreaField, validators, StringField
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    message     = TextField('message:', validators=[validators.required()])
    passcode    = PasswordField('New Password', validators = [validators.DataRequired()])

@app.route("/", methods=['GET', 'POST'])
def user_detail():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        message     =request.form['message']
        passcode    =int(request.form['passcode'])
        print(request.form)
        if form.validate():
            print('inside form')
            try:
                message= E.decryption(message,passcode)
                print(message) 
                flash('Your message has been encrypted successfully.')
            except Exception as e:
                print(e)
                flash('Error: Net Connection is out.')
        else:
            flash('Error: All Fields are Required')

    return render_template('mainPage.html', form=form)

if __name__ == "__main__":
    app.run()