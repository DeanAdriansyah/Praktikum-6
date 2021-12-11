# Program sederhana menggunakan fungsi untuk daftar nilai mahasiswa, dengan ketentuan:

# 1. Fungsi tambah() untuk menambah data
def tambah(nama):
  print("Nama: ", nama, ", Nilai: 100")

tambah("Ari")
nama = "Ari Santoso"
tambah(nama)
  
# 2. Fungsi Tampilkan() untuk menampilkan data
def tampilkan(nama):
  print("nama: ", nama, ", Nilai: 80")
  
tampilkan("Budi")
nama = "Budi Santoso"
tampilkan(nama)

# 3. Fungsi hapus(nama) untuk menghapus data berdasarkan nama
def hapus(nama):
  print("nama: ", nama, ", Nilai: 100")
  
hapus("Ari")
nama = "Ari Santoso"
hapus(nama)

# 4. Fungsi ubah(nama)untuk mengubah data berdasarkan nama
def ubah(nama):
  print("nama: ", nama, ", Nilai: 80")
  
ubah("Anto")
nama = "Anto Santoso"
ubah(nama)
