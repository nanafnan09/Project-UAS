from process.process_buku import ProcessBuku
from view.input_form import InputForm
from view.buku_view import BukuView

def main():
    process_buku = ProcessBuku()

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Semua Buku")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            try:
                judul, penulis, tahun = InputForm.input_data_buku()
                if not judul or not penulis or not tahun:
                    raise ValueError("Semua field harus diisi.")
                process_buku.tambah_buku(judul, penulis, tahun)
                BukuView.tampilkan_message("Buku berhasil ditambahkan.")
            except ValueError as e:
                BukuView.tampilkan_message(f"Error: {e}")

        elif pilihan == '2':
            judul = input("Masukkan judul buku yang ingin dihapus: ")
            if process_buku.hapus_buku(judul):
                BukuView.tampilkan_message("Buku berhasil dihapus.")
            else:
                BukuView.tampilkan_message("Buku tidak ditemukan.")

        elif pilihan == '3':
            buku_list = process_buku.tampilkan_buku()
            BukuView.tampilkan_list(buku_list)

        elif pilihan == '4':
            print("Keluar dari program.")
            break

        else:
            BukuView.tampilkan_message("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()