class InputForm:
    @staticmethod
    def input_data_buku():
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan penulis buku: ")
        tahun = input("Masukkan tahun terbit buku: ")
        return judul, penulis, tahun