from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Fungsi layanan informasi paket tour
def get_tour(tour_id):
    response = requests.get(f'http://localhost:5000/infotour/{tour_id}')
    return response.json()

# Fungsi untuk mendapatkan ulasan berdasarkan tour_id dari API ulasan
def get_reviews(tour_id):
    response = requests.get(f'http://localhost:5003/ulasan/{tour_id}')
    return response.json()


#Route untuk menampilkan informasi paket tour
@app.route('/infotour/<int:tour_id>')
def get_tour_info(tour_id):
    tour_info = get_tour(tour_id)
    tour_reviews = get_reviews(tour_id)
    return render_template('index.html', tour_info=tour_info, tour_reviews=tour_reviews)
     
# Route untuk mendapatkan ulasan berdasarkan tour_id
@app.route('/reviews/<int:tour_id>', methods=['GET'])
def show_reviews(tour_id):
    tour_reviews = get_reviews(tour_id)
    return render_template('index.html', tour_reviews=tour_reviews)

# Route untuk menangani pemesanan tur
@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    try:
        nama = request.form.get('nama')
        email = request.form.get('email')
        nomor_telepon = request.form.get('nomor_telepon')
        paket_tour = request.form.get('paket_tour')
        bulan = request.form.get('bulan')
        jumlah_pax = request.form.get('jumlah_pax')

        data = {
            'nama': nama,
            'email': email,
            'nomor_telepon': nomor_telepon,
            'paket_tour': paket_tour,
            'bulan': bulan,
            'jumlah_pax': jumlah_pax
        }

     # Kirim data ke layanan pemesanan
        response = requests.post('http://localhost:5005/orders', json=data)

        if response.status_code == 201:
            return 'Booking successful', 200
        else:
            return 'Booking failed', 500
    except Exception as e:
        return str(e), 500
    

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)
