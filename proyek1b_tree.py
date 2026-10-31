

# 1.PERANCANGAN STRUKTUR TREE (OOP)
# Skenario: Class Induk (parent) sebagai dasar struktur
class PegawaiNode:
    def __init__(self, id_pegawai, nama, jabatan):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        # pake list untuk mendukung general tree bisa >2 anak
        self.children = [] 

    #  Skenario: fungsi dasar yg nanti akan diubah (override) oleh class turunannya
    def tampilkan_info(self):
        return f"[{self.id_pegawai}] {self.nama} ({self.jabatan})"


# Skenario: Class turunan (child) untuk membedakan tipe posisi di kampus
class PimpinanNode(PegawaiNode):
    def __init__(self, id_pegawai, nama, jabatan, tunjangan="Ada"):
        super().__init__(id_pegawai, nama, jabatan)
        self.tunjangan = tunjangan

    def tampilkan_info(self):
        return f"[{self.id_pegawai}] {self.nama} ({self.jabatan}) - Pimpinan)"

class DosenNode(PegawaiNode):
    def __init__(self, id_pegawai, nama, jabatan, mata_kuliah="Belum Ditentukan"):
        super().__init__(id_pegawai, nama, jabatan)
        self.mata_kuliah = mata_kuliah

    def tampilkan_info(self):
        return f"[{self.id_pegawai}] {self.nama} ({self.jabatan}) - Staf/Akademik)"

class MahasiswaNode(PegawaiNode):
    def __init__(self, id_pegawai, nama, jabatan="Mahasiswa Bimbingan", nim="Belum Diisi"):
        super().__init__(id_pegawai, nama, jabatan)
        self.nim = nim

    # Skenario: Mahasiswa itu daun (leaf) paling bawah di bagan, bukan pegawai
    def tampilkan_info(self):
        return f"[{self.id_pegawai}] {self.nama} (NIM: {self.nim} - Mahasiswa)"


class OrganisasiTree:
    def __init__(self):
        self.root = None

    # 2a. IMPLEMENTASI OPERASI: insert_node()
    # Menyisipkan data baru di bawah atasan tertentu 
    def insert_node(self, nama_atasan, id_pegawai, nama_pegawai, jabatan_pegawai):
        # Skenario: Otomatis nentuin jenis class berdasarkan nama jabatannya
        if "Mahasiswa" in jabatan_pegawai:
            node_baru = MahasiswaNode(id_pegawai, nama_pegawai, jabatan_pegawai)
        elif "Dosen" in jabatan_pegawai or "Asisten" in jabatan_pegawai or "Teknisi" in jabatan_pegawai:
            node_baru = DosenNode(id_pegawai, nama_pegawai, jabatan_pegawai)
        else:
            node_baru = PimpinanNode(id_pegawai, nama_pegawai, jabatan_pegawai)

        if self.root is None:
            self.root = node_baru
            return

        # Skenario: cari posisi atasan dulu, baru masukkan data anak di bawahnya
        atasan = self.search_node(self.root, nama_atasan)
        if atasan:
            atasan.children.append(node_baru)
        else:
            print(f"[!] Gagal! Atasan bernama {nama_atasan} tidak ditemukan.")

    # 2b. IMPLEMENTAASI OPERASI: search_node()
    # Mencari data berdasarkan ID, nama atau jabatan
    def search_node(self, node, keyword):
        if node is None:
            return None

        if node.id_pegawai == keyword or node.nama == keyword or node.jabatan == keyword:
            return node

        for child in node.children:
            hasil = self.search_node(child, keyword)
            if hasil:
                return hasil
        return None

    # 3a. IMPLEMENTASI ALGORITMA TRAVERSAL: Preorder
    # Skenario: Modifikasi khusus untuk General Tree (bukan tree yg cabang)
    def preorder(self, node, level=0):
        if node is None:
            return

        indent = " " * level
        print(f"{indent}-> {node.tampilkan_info()}")

        for child in node.children:
            self.preorder(child, level + 1)

    # 3b. IMPLEMENTASI ALGORITMA TRAVERSAL: Inorder
    def inorder(self, node, level=0):
        if node is None:
            return

        indent = " " * level
        if len(node.children) == 0:
            print(f"{indent}-> {node.tampilkan_info()}")
        else:
            self.inorder(node.children[0], level + 1)
            print(f"{indent}-> {node.tampilkan_info()}")
            for i in range(1, len(node.children)):
                self.inorder(node.children[i], level + 1)

    # 3c.IMPLEMENTASI ALGORITMA TRAVERSAL: Postorder
    def postorder(self, node, level=0):
        if node is None:
            return

        for child in node.children:
            self.postorder(child, level + 1)

        indent = " " * level
        print(f"{indent}-> {node.tampilkan_info()}")