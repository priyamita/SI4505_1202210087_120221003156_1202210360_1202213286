from flask import Flask, jsonify, request

app = Flask(__name__)

# Data sampel (di dalam memori)
ulasan_produk = [
    {"user_id": 1, "tour_id": 1, "review": "Tour travelnya murah sekali, rute destinasi jelas dan ontime."},
    {"user_id": 3, "tour_id": 3, "review": "Informasi yang diberikan sangat jelas, memberikan pengetahuan juga tiap mengunjungi tempat bersejarah."},
    {"user_id": 2, "tour_id": 2, "review": "Jadwal perjalanan yang beragam dan menarik. Sangat puas dengan pelayanannya pokoknya."},
    {"user_id": 2, "tour_id": 1, "review": "Agen travel sangat memperhatikan keselamatan dan kesehatan paket tour, recommended pokoknya!"}
]

# Mendapatkan semua ulasan
@app.route('/ulasan', methods=['GET'])
def get_all_reviews():
    return jsonify(ulasan_produk)

# Mendapatkan ulasan berdasarkan ID produk
@app.route('/ulasan/<int:tour_id>', methods=['GET'])
def get_reviews_by_product(tour_id):
    reviews = [review for review in ulasan_produk if review['tour_id'] == tour_id]

    if reviews:
        return jsonify({"tour_id": tour_id, "reviews": reviews})
    else:
        return jsonify({"message": "Produk tidak ditemukan"}), 404

# Menambahkan ulasan baru
@app.route('/ulasan', methods=['POST'])
def add_review():
    data = request.get_json()
    if not all(key in data for key in ['user_id', 'tour_id', 'review']):
        return jsonify({"message": "Data yang diperlukan tidak lengkap"}), 400

    ulasan_produk.append(data)
    return jsonify({"message": "Ulasan berhasil ditambahkan"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
