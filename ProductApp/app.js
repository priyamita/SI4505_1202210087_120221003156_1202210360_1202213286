const express = require("express")
const app = express()

const infotour = [
    {id:1, paket:"Bandung", destinasi: "Gedung Sate, Observatorium Bosscha, Braga, Ranca Upas, Kawah Putih Ciwidey", fasilitas: "Penginapan The Trans Luxury Hotel, Titik Jemput Bandara Soekarno Hatta, Free Makan, Pusat Oleh-oleh", estimasi: "2 hari", harga: "Rp 9.000.000/pax"},
    {id:2, paket:"Malang", destinasi: "Gunung Bromo, Kampung Heritage, Bakso President, Jatim Park, Museum Angkut, BNS", fasilitas: "Penginapan Grand Mercure Malang Mirama, Titik Jemput Bandara Juanda, Free Makan, Pusat Oleh-oleh", estimasi: "3 hari", harga: "Rp 8.000.000/pax"},
    {id:3, paket:"Bali", destinasi: "Pantai Melasti, Pantai Pandawa, Jimbaran, GWK, Ubud, Tanah Lot, Bedugul, Nusa Dua", fasilitas: "Penginapan Ayana Resort Bali, Titik Jemput Bandara Ngurah Rai, Free Makan, Pusat Oleh-oleh", estimasi: "4 hari", harga: "Rp 10.000.000/pax"},
    //{id:2, paket:"Malang", destinasi: "Gunung Bromo, Kampung Heritage, Bakso President, Jatim Park, Museum Angkut, BNS", fasilitas: "Penginapan Grand Mercure Malang Mirama, Titik Jemput Bandara Juanda, Free Makan, Pusat Oleh-oleh", estimasi: "3 hari", harga: "Rp 8.000.000/pax"},
    //{id:3, paket:"Bali", destinasi: "Pantai Melasti, Pantai Pandawa, Jimbaran, GWK, Ubud, Tanah Lot, Bedugul, Nusa Dua", fasilitas: "Penginapan Ayana Resort Bali, Titik Jemput Bandara Ngurah Rai, Free Makan, Pusat Oleh-oleh", estimasi: "4 hari", harga: "Rp 10.000.000/pax"}
]

app.get('/infotour',(req, res) => {
    res.json(infotour)
})

app.get('/infotour/:tour_id', (req, res) => {
    const tourId = parseInt(req.params.tour_id)
    const tour =  infotour.find(tour => tour.id === tourId)

    if(tour){
        res.json(tour)
    }else{
        res.status(404),json({error: "Paket tidak ditemukan"})
    }

})

app.listen(5000, () => {
    console.log("server berjalan")
})