# app.py
from flask import Flask, render_template, redirect, url_for, request
from user import User

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/')
def read_all():
    users = User.get_all()
    print(users)
    return render_template('index.html', users = users)

# @app.route("/users/add")
# def add_user():
#     return render_template("create_user.html")

@app.route("/users/add", methods=['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        # add record to database
        User.save(request.form)
        return redirect("/")
    if request.method == 'GET':
        return render_template("create_user.html")



if __name__ == '__main__':
    app.run(debug=True)