#Belajar Tipe data Dictionary
# dictionary = agar kita tidak melakukan kesalahan dalam mengakses datanya.

customer = {"Nama": "Budi", "Umur": 34, "Alamat": "Bandung"}

# cara mengakses data dictionary :
# print(customer["Nama"])
# print(customer["Umur"])
# print(customer["Alamat"])

# method dalam dict items() = utk mengambil semua key value dalam bentuk tuple.
# print(customer.items())

# mengubah data dict :
customer["Nama"] = "Jeri"

# menambah data dict :
customer["Hobi"] = "main catur"

# menghapus data dict :
del customer["Alamat"]

# mengakses data pakai looping :
for key, value in customer.items():
    print(f'{key} : {value}')
