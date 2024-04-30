from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3309
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pesantour'

mysql = MySQL(app)

# Route untuk menambah data pemesanan paket tour
@app.route('/orders', methods=['POST'])
def add_order():
    try:
        data = request.json
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO orders (nama, email, nomor_telepon, paket_tour, bulan, jumlah_pax) VALUES (%s, %s, %s, %s, %s, %s)", (data['nama'], data['email'], data['nomor_telepon'], data['paket_tour'], data['bulan'], data['jumlah_pax']))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Order added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route untuk melihat daftar keseluruhan database
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM orders")
        result = cursor.fetchall()
        cursor.close()
        return jsonify({'orders': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route untuk mencari pesanan berdasarkan ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        order = cursor.fetchone()
        cursor.close()
        if order:
            return jsonify({'order': order}), 200
        else:
            return jsonify({'message': 'Order not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
