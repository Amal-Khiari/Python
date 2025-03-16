# flask_app/controllers/users.py
from flask import render_template, redirect, request
from flask_app.models.user import User

def create_user():
    if request.method == 'POST':
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }
        User.create(data)
        return redirect('/users')
    return render_template('user.html')