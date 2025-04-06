from flask import Flask ,  render_template, request, redirect, session, flash
app= Flask(__name__)

app.secret_key = 'your_secret_key_here'  # Required for session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Store form data in session
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form.get('comments', '')  # Optional field
    
    # Check for radio button (Ninja Bonus)
    session['experience'] = request.form.get('experience', 'Not specified')
    
    # Check for checkboxes (Sensei Bonus)
    session['interests'] = request.form.getlist('interests') or ['None']
    
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

