# membuat program menggunakan for loop, list dan range

banyak = int(input('berapa banyak data? :'))

nama = []
umur = []

for i in range(0, banyak):
    print(f'data ke-{i}')
    input_nama = input('nama anda : ')
    input_umur = int(input('umur anda : '))
    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f'nama saya {data_nama} dan umur saya {data_umur} tahun')