from flask import Flask
import random
import requests

app = Flask(__name__)

@app.route("/")
def main_page():
    return f'''<h1>Halo, User!</h1>
                <h2>Di halaman ini, kalian dapat mengetahui beberapa fakta tentang teknologi!</h2>
                <h4><a href="/fakta_teknologi">Klik di sini untuk fakta!</a></h4>
                <h4><a href="/random_password">Kilik di sini untuk password acak!</a></h4>
                <h4><a href="/coin_flip">Kilik di sini untuk coin flip!</a></h4>
                <h4><a href="/duck_photo">Kilik di sini untuk foto bebek!</a></h4>'''

@app.route("/fakta_teknologi")
def facts():
    facts_list = ['Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka',
                  'Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
                  'Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan',
                  'Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja',
                  'Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati',
                  'Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten',
                  'Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita',
                  'Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini']
    return f'''<h3>Fakta Teknologi : {random.choice(facts_list)}</h3>
                <h5>(Pencet "Ctrl+R" secara bersamaan untuk memuat ulang website dan mendapatkan fakta baru! Atau klik <a href="/fakta_teknologi">di sini!</a>)</h5>
                <h4><a href="/">Klik di sini untuk kembali ke halaman utama!</a></h4>'''

@app.route("/random_password")
def gen_pass():
    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(10):
        password+=random.choice(characters)
    
    return f'''<h2>Password Acak : {password}</h2><h5>(Pencet "Ctrl+R" secara bersamaan untuk memuat ulang website dan mendapatkan sandi acak baru! Atau klik <a href="/random_password">di sini!</a>)</h5>
            <h4><a href="/">Klik di sini untuk kembali ke halaman utama!</a></h4>'''

@app.route("/coin_flip")
def coin_flip():
    return f'''<h2>Hasil coin flip : {random.choice(["Heads", "Tails"])}
            <h5>(Pencet "Ctrl+R" secara bersamaan untuk memuat ulang website dan mendapatkan hasil baru! Atau klik <a href="/coin_flip">di sini!</a>)</h5>
            <h4><a href="/">Klik di sini untuk kembali ke halaman utama!</a></h4>'''

@app.route("/duck_photo")
def duck_photo():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()

    return f'''<h1>Foto bebek : <img src="{data['url']}" width="450" height="350"></h1>
            <h3>(Pencet "Ctrl+R" secara bersamaan untuk memuat ulang website dan mendapatkan foto baru! Atau klik <a href="/duck_photo">di sini!</a>)</h3>
            <h2><a href="/">Klik di sini untuk kembali ke halaman utama!</a></h2>'''

app.run(debug=True)