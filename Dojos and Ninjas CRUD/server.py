from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'dojos_and_ninjas_schema'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
@app.route('/dojos')
def dojos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dojos")
    dojos = cur.fetchall()
    cur.close()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    name = request.form['name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO dojos (name) VALUES (%s)", (name,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dojos'))

@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dojos WHERE id = %s", (dojo_id,))
    dojo = cur.fetchone()
    cur.execute("SELECT * FROM ninjas WHERE dojo_id = %s", (dojo_id,))
    ninjas = cur.fetchall()
    cur.close()
    return render_template('dojo_show.html', dojo=dojo, ninjas=ninjas)

@app.route('/ninjas')
def ninjas():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dojos")
    dojos = cur.fetchall()
    cur.close()
    return render_template('ninjas.html', dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    dojo_id = request.form['dojo_id']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, age, dojo_id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dojo_show', dojo_id=dojo_id))

if __name__ == '__main__':
    app.run(debug=True)