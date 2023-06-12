import requests
import random
import time
import concurrent.futures

def bypass_page_cache(url, num_requests, delay):
    # Membuat session untuk mempertahankan koneksi yang sama
    session = requests.Session()

    # Membuat permintaan awal untuk menginisialisasi session
    session.get(url)

    # Header untuk melewati cache halaman dan mengatur User-Agent
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    # Mengirim permintaan sejumlah num_requests untuk menguji beban menggunakan multi-threading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Fungsi untuk mengirim permintaan secara konkuren dalam satu thread
        def send_request(url, request_number):
            response = session.get(url, headers=headers)
            print(f"Request {request_number} - Status code: {response.status_code}")

            # Lakukan tindakan lain yang diperlukan berdasarkan respons

        # Membuat daftar URL dengan query acak
        urls = [f"{url}?random={random.randint(1, 1000000)}" for _ in range(num_requests)]

        # Mengirim permintaan konkuren dengan multi-threading
        executor.map(send_request, urls, range(1, num_requests + 1))

    # Menutup session setelah selesai
    session.close()

# Contoh pemanggilan fungsi bypass_page_cache
url = 'https://contoh.com'  # Ganti dengan URL situs WordPress yang ingin diuji
num_requests = 100  # Jumlah permintaan yang ingin dikirim
delay = 1  # Waktu jeda antara permintaan (dalam detik)
bypass_page_cache(url, num_requests, delay)
