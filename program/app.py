# Program Management Kontak
import function

# List of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama": "ujang",
    "email": "ujang11@gmail.com",
    "telepon": "08787089898",
})

while True:
    print('# Menu')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Hapus Kontak')
    print('4. Cari Kontak')
    print('0. Keluar Kontak')

    Menu = input('pilih menu : ')

    if Menu == '0':
        break
    elif Menu == '1':
        function.display_kontak(daftar_kontak)
    elif Menu == '2':
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif Menu == '3':
        function.hapus_kontak(daftar_kontak)
    elif Menu == '4':
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")

print('program selesai berjalan, sampai jumpa')
