# Belajar Module

def say_hello(nama):
    return f'hello {nama}'

def total(*list_angka):
    total = 0
    for data in list_angka:
        total = total + data
    return total