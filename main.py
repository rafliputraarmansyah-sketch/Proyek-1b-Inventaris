# Import class dari file silsilah_organisasi.py
from proyek1b_tree import OrganisasiTree

def main():
    tree = OrganisasiTree()

    print("=== PROSES INSERT DATA SILSILAH ORGANISASI ===")
    # Skenario: Membangun struktur organisasi UIN Suska Riau sesuai bagan gambar (Root = Rektor)
    
    # Tingkat 1 & 2
    tree.insert_node(None, "R-01", "Prof. Fulan", "Rektor")
    tree.insert_node("Prof. Fulan", "SU-01", "Ketua Senat", "Senat Universitas")
    tree.insert_node("Prof. Fulan", "WR-1", "Dr. Akademik", "Wakil Rektor I")
    tree.insert_node("Prof. Fulan", "WR-2", "Dr. Keuangan", "Wakil Rektor II")
    tree.insert_node("Prof. Fulan", "WR-3", "Dr. Kemahasiswaan", "Wakil Rektor III")
    tree.insert_node("Prof. Fulan", "DK-01", "Dr. Siti", "Dekan Fakultas Sains dan Teknologi")

    # Tingkat 3 (Bawahan Dekan)
    tree.insert_node("Dr. Siti", "WD-1", "Pak WD 1", "Wakil Dekan I")
    tree.insert_node("Dr. Siti", "WD-2", "Pak WD 2", "Wakil Dekan II")
    tree.insert_node("Dr. Siti", "WD-3", "Pak WD 3", "Wakil Dekan III")
    tree.insert_node("Dr. Siti", "KP-01", "Pak Andi", "Ketua Program Studi Teknik Informatika")

    # Tingkat 4 (Bawahan Ketua Prodi)
    tree.insert_node("Pak Andi", "SP-01", "Bu Sekprodi", "Sekretaris Program Studi")
    tree.insert_node("Pak Andi", "KL-01", "Pak Joko", "Kepala Laboratorium Komputer")
    tree.insert_node("Pak Joko", "AL-01", "Kak Aslab", "Asisten Laboratorium")
    tree.insert_node("Pak Joko", "TL-01", "Pak Teknisi", "Teknisi Laboratorium")

    tree.insert_node("Pak Andi", "KD-01", "Bu Rina", "Koordinator Dosen")
    tree.insert_node("Bu Rina", "PA-01", "Pak Budi", "Dosen Pembimbing Akademik")
    
    # Skenario: Mahasiswa Bimbingan ditambahkan, bertindak sebagai leaf di ujung bagan
    tree.insert_node("Pak Budi", "M-01", "Rafli Putra", "Mahasiswa Bimbingan")
    tree.insert_node("Bu Rina", "MK-01", "Pak Pengampu", "Dosen Pengampu Mata Kuliah")
    
    print("[*] Semua data berhasil dimasukkan ke dalam Tree.\n")

    # Skenario: Pengujian 3 metode Traversal sesuai instruksi lembar aktivitas
    print("=== [1] PRE-ORDER TRAVERSAL ===")
    tree.preorder(tree.root)
    
    print("\n=== [2] IN-ORDER TRAVERSAL ===")
    tree.inorder(tree.root)
    
    print("\n=== [3] POST-ORDER TRAVERSAL ===")
    tree.postorder(tree.root)

if __name__ == "__main__":
    main()