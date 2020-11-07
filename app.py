from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# mysql database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactosdb'  # o cualquier otro nombre
mysql = MySQL(app)

app.secret_key='mysecretkey' # o cualquier otro nombre

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos')
    data = cur.fetchall()
    return render_template('index.html', contactos=data)
    #return 'Index - Diseño de software-UTEC'

@app.route('/add_contact')
def add_contact():
    return 'Contacto'
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)  # o cualquiero otro puerto


