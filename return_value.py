# Belajar Method Return Value

# return = mengembalikan nilai

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (total)

total = jumlahkan(10, 10, 12)
print(total)


