import time
import winsound  # Modul ini hanya untuk Windows, untuk sistem operasi lain gunakan modul yang sesuai

def timer(jam, menit, detik, custom_message=None):
    total_detik = jam * 3600 + menit * 60 + detik

    while total_detik >= 0:
        jam = total_detik // 3600
        sisa_detik = total_detik % 3600
        menit = sisa_detik // 60
        detik = sisa_detik % 60

        print(f"{jam:02d}:{menit:02d}:{detik:02d}", end="\r")
        time.sleep(1)
        total_detik -= 1

    print(custom_message or "Waktu habis!")
    if custom_message:
        print("Pesan kustom:", custom_message)
    play_sound()  # Memanggil fungsi untuk memainkan suara alarm

def play_sound():
    try:
        frequency = 1500  # Frekuensi alarm (1500 Hz)
        duration = 3000   # Durasi alarm dalam milidetik (3 detik)
        winsound.Beep(frequency, duration)
    except Exception as e:
        print(f"Error playing sound: {e}")

# Fungsi untuk menjalankan timer berulang kali
def run_timer():
    while True:
        jam_input = int(input("Masukkan jumlah jam: "))
        menit_input = int(input("Masukkan jumlah menit: "))
        detik_input = int(input("Masukkan jumlah detik: "))
        pesan_kustom = input("Masukkan pesan kustom (biarkan kosong untuk menggunakan pesan default): ")

        timer(jam_input, menit_input, detik_input, pesan_kustom)
        print("\nTimer Selesai!\n")

        ulangi = input("Apakah Anda ingin mengulang timer? (y/n): ")
        if ulangi.lower() != 'y':
            break  # Berhenti dari loop jika tidak ingin melanjutkan

# Jalankan program
run_timer()