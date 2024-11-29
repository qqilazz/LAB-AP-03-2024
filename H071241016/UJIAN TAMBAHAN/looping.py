tinggi = int(input("Masukkan tinggi segitiga: "))

if tinggi <= 0:
    print("Tinggi segitiga harus positif.")
else:
    for i in range(tinggi, 0, -1):
        print("*" * i)