import re
def validasi_nomor_telepon(nomor):
  pola = r"^\+62\d{8,12}$"

  if re.match(pola, nomor):
    return True
  else:
    return False

if __name__ == "__main__":
  nomor_telepon = input("Masukkan nomor telepon: ")
  if validasi_nomor_telepon(nomor_telepon):
    print("Nomor telepon anda valid")
  else:
    print("Nomor telepon anda tidak valid")
    print("silahkan coba lagi!!!!")