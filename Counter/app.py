from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html', visits=session['visits'], counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment', methods=['POST'])
def increment():
    increment_by = int(request.form['increment'])
    session['counter'] += increment_by
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)