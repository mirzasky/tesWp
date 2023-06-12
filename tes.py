import requests
import random
import time

def bypass_page_cache(url, num_requests, delay):
    # Membuat session untuk mempertahankan koneksi yang sama
    session = requests.Session()

    # Membuat permintaan awal untuk menginisialisasi session
    session.get(url)

    # Header untuk melewati cache halaman
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0'
    }

    # Mengirim permintaan sejumlah num_requests untuk menguji beban
    for i in range(num_requests):
        # Menambahkan query acak pada URL
        random_query = str(random.randint(1, 1000))
        request_url = url + "?random=" + random_query

        response = session.get(request_url, headers=headers)
        print("Request", i+1, "- Status code:", response.status_code)

        # Lakukan tindakan lain yang diperlukan berdasarkan respons

        # Menunggu waktu jeda antara permintaan
        time.sleep(delay)

    # Menutup session setelah selesai
    session.close()

# Contoh pemanggilan fungsi bypass_page_cache
url = 'https://www.example.com'  # Ganti dengan URL situs WordPress yang ingin diuji
num_requests = 10  # Jumlah permintaan yang ingin dikirim
delay = 1  # Waktu jeda antara permintaan (dalam detik)
bypass_page_cache(url, num_requests, delay)
