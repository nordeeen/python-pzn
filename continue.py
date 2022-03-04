# Belajar Continue

#continue = untuk menghentikan perulangan, lalu melanjutkan perulangan selanjutnya
# nilai % 2 == 0 -> ganjil
# nilai % 2 == 1 -> genap

for i in range(1,100):
    if i % 2 == 0:
        continue
    print(i)