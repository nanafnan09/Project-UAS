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