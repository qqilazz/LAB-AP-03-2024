from functools import reduce
def hitung_jumlah_genap(angka_list):
  angka_genap = list(filter(lambda x: x % 2 == 0, angka_list))
  jumlah_genap = reduce(lambda x, y: x + y, angka_genap)
  return jumlah_genap

angka = [1, 2, 3, 4, 5, 6]
hasil = hitung_jumlah_genap(angka)
print("Jumlah angka genap:", hasil)