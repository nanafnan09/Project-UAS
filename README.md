# Project-UAS

Nama: Afnan Dika Ramadhan

NIM: 312410518

Kelas: TI24.A5

MATAKULIAH: BAHASA PEMROGRAMAN

Struktur Program

Program ini terdiri dari beberapa file yang terpisah berdasarkan fungsinya:

1.	Data: Menyimpan kelas yang merepresentasikan data.

2.	Process: Menangani logika pemrosesan data.

3.	View: Menangani tampilan dan interaksi dengan pengguna.

4.	Main: File utama yang menjalankan program.

# 1. data/buku.py
```python
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"{self.judul} oleh {self.penulis} ({self.tahun})"
```

 Kelas Buku:
•	Tujuan: Mewakili objek buku dengan atribut yang relevan.
`	__init__:`

 Ini adalah konstruktor yang dipanggil saat objek Buku dibuat.

 Parameter:

 judul: Judul buku.

 penulis: Nama penulis buku.

 tahun: Tahun terbit buku.

  Atribut self.judul, self.penulis, dan self.tahun diinisialisasi dengan nilai yang diberikan saat objek dibuat.

 `__str__:`

Metode ini mengembalikan representasi string dari objek Buku.

Ketika Anda mencetak objek Buku, metode ini akan dipanggil, dan hasilnya akan menampilkan judul, penulis, dan tahun terbit dalam format yang mudah dibaca

# 2. `data/databuku.py`

```python
class DataBuku:
    def __init__(self):
        self.buku_list = []

    def tambah_buku(self, judul, penulis, tahun):
        buku = Buku(judul, penulis, tahun)
        self.buku_list.append(buku)

    def hapus_buku(self, judul):
        for buku in self.buku_list:
            if buku.judul == judul:
                self.buku_list.remove(buku)
                return True
        return False

    def tampilkan_buku(self):
        return self.buku_list

```
Kelas DataBuku:

Tujuan: Mengelola daftar buku, termasuk menambah, menghapus, dan menampilkan buku.
`__init__:`

Menginisialisasi atribut buku_list, yang merupakan daftar kosong untuk menyimpan objek Buku.
`tambah_buku:`

Metode ini menerima judul, penulis, dan tahun sebagai parameter.
Membuat objek Buku baru dengan parameter yang diberikan dan menambahkannya ke dalam buku_list.
`hapus_buku:`

Mencari buku berdasarkan judul dalam buku_list.
Jika buku ditemukan, buku tersebut dihapus dari daftar dan metode mengembalikan True.
Jika tidak ditemukan, metode mengembalikan False.
tampilkan_buku:
Mengembalikan daftar semua buku yang ada dalam buku_list.

# 3.`. process/process_buku.py`
```python
from data.databuku import DataBuku

class ProcessBuku:
    def __init__(self):
        self.data_buku = DataBuku()

    def tambah_buku(self, judul, penulis, tahun):
        self.data_buku.tambah_buku(judul, penulis, tahun)

    def hapus_buku(self, judul):
        return self.data_buku.hapus_buku(judul)

    def tampilkan_buku(self):
        return self.data_buku.tampilkan_buku()

```
Kelas ProcessBuku:

Tujuan: Menyediakan antarmuka untuk berinteraksi dengan data buku.
`__init__:`

Membuat instance dari DataBuku, yang akan digunakan untuk mengelola data buku.
`tambah_buku:`

Memanggil metode tambah_buku dari DataBuku untuk menambahkan buku baru.
`hapus_buku:`

Memanggil metode hapus_buku dari DataBuku untuk menghapus buku berdasarkan judul.
`tampilkan_buku:`

Memanggil metode tampilkan_buku dari DataBuku untuk mendapatkan daftar buku.

4.`view/input_form.py`

```python
class InputForm:
    @staticmethod
    def input_data_buku():
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan penulis buku: ")
        tahun = input("Masukkan tahun terbit buku: ")
        return judul, penulis, tahun

```

Kelas InputForm:

Tujuan: Mengelola input data dari pengguna.
`input_data_buku:`
Metode statis yang meminta pengguna untuk memasukkan informasi tentang buku.
Menggunakan fungsi input() untuk meminta pengguna memasukkan:

judul: Judul buku.

penulis: Nama penulis buku.

tahun: Tahun terbit buku.

Metode ini mengembalikan tuple yang berisi judul, penulis, dan tahun yang dimasukkan oleh pengguna.

# 5.view/buku_view.py
```python
class BukuView:
    @staticmethod
    def tampilkan_list(buku_list):
        print(f"{'Judul':<30} {'Penulis':<20} {'Tahun':<10}")
        print("-" * 60)
        for buku in buku_list:
            print(f"{buku.judul:<30} {buku.penulis:<20} {buku.tahun:<10}")

    @staticmethod
    def tampilkan_message(message):
        print(message)
```
Kelas BukuView:

Tujuan: Menangani tampilan dan output ke pengguna.
`tampilkan_list:`

Metode statis yang menerima daftar buku (buku_list) dan menampilkan informasi buku dalam format tabel.
Menggunakan format string untuk menyusun kolom dengan lebar tertentu:

'Judul', 'Penulis', dan 'Tahun' ditampilkan sebagai header.
Menggunakan loop untuk mencetak setiap buku dalam daftar dengan format yang sama.

tampilkan_message:
Metode statis yang menerima pesan sebagai parameter dan mencetaknya ke layar.
Berguna untuk memberikan umpan balik kepada pengguna, seperti konfirmasi atau pesan kesalahan.

# 6. main.py
```python
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

```
Fungsi main:

Tujuan: Menjalankan program dan mengelola interaksi dengan pengguna.
process_buku:

Membuat instance dari ProcessBuku, yang akan digunakan untuk mengelola data buku.
Loop while True:

Menampilkan menu utama kepada pengguna dan meminta input untuk memilih opsi.

Opsi yang tersedia:

Tambah Buku: Meminta pengguna untuk memasukkan data buku dan menambahkannya ke dalam daftar.
Menggunakan try-except untuk menangani validasi input. Jika ada field yang kosong, akan




