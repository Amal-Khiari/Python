from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard_default():
    return render_template('checkerboard.html', rows=8, cols=8)

@app.route('/<int:x>')
def checkerboard_x(x):
    return render_template('checkerboard.html', rows=8, cols=x)

@app.route('/<int:x>/<int:y>')
def checkerboard_x_y(x, y):
    return render_template('checkerboard.html', rows=x, cols=y)

if __name__ == "__main__":
    app.run(debug=True)