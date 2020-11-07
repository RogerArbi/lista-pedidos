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

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nom = request.form['nombres']
        tel = request.form['telefono']
        email = request.form['email']
        print('UPDATE', id, nom, tel,  email)
        cur= mysql.connection.cursor()
        cur.execute('insert into contactos(nombres,telefono,email) values(%s, %s, %s)', (nom,tel,email))
        mysql.connection.commit()
        flash('Contacto insertado correctamente')
        return redirect(url_for('index'))
    
@app.route('/edit/<id>')
def edit_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos where id = %s', {id})
    data = cur.fetchall()
    print(data[0])    
    return render_template('edit.html', contacto=data[0])

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from contactos where id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado correctamente')
    return redirect(url_for('index'))
    
@app.route('/update/<id>',methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        nom = request.form['nombres']
        tel = request.form['telefono']
        email = request.form['email']
        print('UPDATE', id, nom, tel,  email)
        cur = mysql.connection.cursor()
        cur.execute("""
            update contactos
            set nombres = %s,
            telefono = %s,
            email = %s
            where id = %s
        """, (nom, tel, email, id) )
        mysql.connection.commit()
        flash('Contacto actualizado correctamente')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)  # o cualquiero otro puerto


