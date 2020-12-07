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
    cur.execute('select count(*) from contactos')
    data = cur.fetchall()
    return render_template('index.html', contactos=data)
    #return 'Index - Diseño de software-UTEC'


# SELECT count(*) AS TOTALNUMBEROFTABLES
#    -> FROM INFORMATION_SCHEMA.TABLES
#    -> WHERE TABLE_SCHEMA = 'business';



@app.route('/carrito')
def carrito():
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos')
    data = cur.fetchall()
    return render_template('carrito.html', contactos=data)
    #return 'Index - Diseño de software-UTEC'

@app.route('/add_contact', methods=['POST'])
def add_contact():
    # if request.method == 'POST':
    #     nom = request.form['nombres']
    #     tel = request.form['telefono']
    #     email = request.form['email']
    #     print('UPDATE', id, nom, tel,  email)
    #     cur= mysql.connection.cursor()
    #     cur.execute('insert into contactos(nombres,telefono,email) values(%s, %s, %s)', (nom,tel,email))
    #     mysql.connection.commit()
    #     flash('Contacto insertado correctamente')
    #     return redirect(url_for('index'))
    if request.method == 'POST':
        producto = request.form['producto']
        cantidad = request.form['cantidad']
        marca = request.form['marca']
        tamanio = request.form['tamanio']
        print('UPDATE', id, producto, cantidad, marca, tamanio)
        cur= mysql.connection.cursor()
        cur.execute('insert into contactos(producto, cantidad, marca, tamanio) values(%s, %s, %s, %s)', (producto, cantidad, marca, tamanio))
        mysql.connection.commit()
        flash('Producto insertado correctamente')
        return redirect(url_for('carrito'))
    
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
    flash('Producto eliminado correctamente')
    return redirect(url_for('carrito'))

@app.route('/limpiar/')
def limpiar_contact():
    cur = mysql.connection.cursor()
    cur.execute('delete from contactos')
    mysql.connection.commit()
    flash('Todos los productos de la lista han sido eliminados')
    return redirect(url_for('carrito'))

@app.route('/envio/')
def envio_contact():
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos')
    data = cur.fetchall()
    
    return render_template('envio.html', contactos=data)
    flash('Su lista de productos ha sido enviada a las tiendas más cercanas. Pronto recibirá la aceptación de su pedido.')
    
@app.route('/update/<id>',methods=['POST'])
def update_contact(id):

    if request.method == 'POST':
        producto = request.form['producto']
        cantidad = request.form['cantidad']
        marca = request.form['marca']
        tamanio = request.form['tamanio']
        print('UPDATE', id, producto, cantidad, marca, tamanio)
        cur = mysql.connection.cursor()
        cur.execute("""
            update contactos
            set producto = %s,
            cantidad = %s,
            marca = %s,
            tamanio = %s
            where id = %s
        """, (producto, cantidad, marca, tamanio, id) )
        mysql.connection.commit()
        flash('Lista de productos actualizada correctamente')
        return redirect(url_for('carrito'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)  # o cualquiero otro puerto


