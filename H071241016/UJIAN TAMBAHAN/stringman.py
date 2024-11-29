def permutasi_rekursif(s):
    if len(s) <= 1:
        return [s]

    result = []
    for i in range(len(s)):
        karakter_pertama = s[i]
        remaining_karakter = s[:i] + s[i+1:]
        for p in permutasi_rekursif(remaining_karakter):
            result.append(karakter_pertama + p)

    return sorted(set(result))  

string = "abc"
print(permutasi_rekursif(string))