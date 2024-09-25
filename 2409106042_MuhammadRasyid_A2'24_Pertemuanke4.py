# ulang = 10
# for i in range(ulang) :
#     print("Perulangan ke-" + str(i))

# rasyid = 21
# for i in range(rasyid) :
#     print("Muhammad Rasyid" + str(i))

# for j in range(2, 12):
#     print("Halo")
# print("Hai")

# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print(i)

# print("Menu rumah makan informatika")
# print("----------------------------")
# menu = ["-Nasi goreng", "-Mie goreng", "-Mie ayam", "-Bakso", "-Soto"]
# for i in menu:
#     print(i)

# print("Menu rumah makan informatika")
# print("----------------------------")
# menu = ["Nasi goreng", "Mie goreng", "Mie ayam", "Bakso", "Soto"]
# for i, menu in enumerate(menu,start=1):
#     print(f"{i}.{menu}")

# print("Menu rumah makan informatika")
# print("----------------------------")
# simpan = ["Nasi goreng", "Mie goreng", "Mie ayam", "Bakso", "Soto"]
# for i in range(len(simpan)):
#     print(f"{i+1}.{simpan[i]}")

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()

# makanan = ["mie", "nasi", "telor"]
# minuman = ["airputih", "esteh", "esjruk"]

# for i in makanan:
#     for j in minuman:
#         print(f"{i} & {j}")

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya' or jawab == 'Ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}")

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih Ingin Mengulang? ")
#     if ulang == "tidak" or ulang =="Tidak":
#         break
# print(f"Total Perulangan: {hitung}")

# continue
# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih Ingin Lanjut? ")
#     if ulang == "y" or ulang =="Y":
#         print("Oke Kita Lanjut")
#         continue

# print(f"Total Perulangan: {hitung}")

# print("Daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# studi kasus 1
# total = 0
# while True:
#     angka = int(input("Masukkan angka positif (input negatif jika ingin berhenti): "))
#     if angka < 0:
#         break
#     total += angka

# print("Jumlah total adalah:", total)

# studi kasus 2

# Meminta input dari pengguna untuk range maksimal
range_maksimal = int(input("Masukkan range maksimal: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan prima
hitung_prima = 0

# Loop untuk memeriksa setiap angka dari 1 hingga range_maksimal
for angka in range(1, range_maksimal):
    angka += 1
    apakah_prima = True  # Anggap angka tersebut prima

    # Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
    for i in range(2, angka):
        if angka % i == 0:
            apakah_prima = False  # Jika ada pembagi, bukan bilangan prima
            # print(f"{angka} bukan prima")
            break
    # Jika angka tersebut prima, tambahkan jumlah hitung_prima
    if apakah_prima == True:
        print(f"{angka} prima")
        hitung_prima += 1

# output
print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")
