import re

input_string = input("Masukkan string (45 karakter): ")

if len(input_string) != 45:
    print(False)
else:
    if not re.match(r'^^[A-z0-9]{40}[13579\s]{5}$',input_string):
        print(False)
    else:
        print(True)