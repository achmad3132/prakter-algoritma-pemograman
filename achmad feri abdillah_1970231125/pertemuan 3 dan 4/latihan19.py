#Latihan
# kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")
angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukan angka 2 = "))

# percabangannya
if operator == "+": hasil = angka_1 + angka_2
print(f"hasilnya adalah {hasil}")

if operator == "-":hasil = angka_1 - angka_2
print(f"hasilnya adalah {hasil}")

if operator == "x" or operator == "*": hasil = angka_1 * angka_2
print(f"hasilnya adalah {hasil}")

if operator == "/": hasil = angka_1 / angka_2
print(f"hasilnya adalah {hasil}")

print("masukan yang bener dong!, aku pusying")

print("Akhir dari program, terima gajih!")

# for kondisi:
# aksi

# ini dengan list
angka2_list = [0,2,4,8,10] # ini adalah list
print(angka2_list)

for i in angka2_list: print(f"i sekarang -> {i}")
print("akhir dari program 1 \n")

# ini dengan range
angka2_range = range(5)
for i in angka2_range: print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")
angka2_range = range(1,10)
for i in angka2_range: print(f"i sekarang -> {i}")
# print("saya keren")

print("akhir dari program 3 \n")
# menggunakan string
data_str = "saya ganteng abiees"
for huruf in data_str: print(huruf)

print("akhir dari program 4 \n")