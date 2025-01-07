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