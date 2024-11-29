try:
    umur = int(input("Masukkan umur: "))

    if umur < 12:
        print("Anda adalah seorang anak-anak")
    elif 12 <= umur <= 17:
        print("Anda adalah seorang remaja")
    elif 18 <= umur <= 64:
        print("Anda adalah seorang dewasa")
    elif umur > 64:
        print("Anda adalah seorang lansia")
    else:
        print("Umur tidak valid")
except ValueError:
    print("Umur harus berupa angka")