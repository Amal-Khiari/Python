from flask import Flask, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management
if __name__ == '__main__':
    app.run(debug=True)