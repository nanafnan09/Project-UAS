from .buku import Buku

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