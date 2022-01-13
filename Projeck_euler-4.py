def palindromic(angka): # befungsi untuk memastikan angka adalah palindromic
    return str(angka) == str(angka)[::-1] #str(angka)[::-1] membalik angka dengan membandingkan kebalikannya

hasil = 0 # tempat menyimpan hasil
for i in range(999,99,-1): # mundur di buat mundur agar perhitungan lebih cepat 
    for j in range(999,99,-1):
        angka = i*j 
        if palindromic(angka)and angka>hasil:#memastika nilai palindromic terbesar
            hasil = angka

print (hasil)
"""angka polindormic adalah angka yang jika di balik bernilai sama contoh 131,202,9009,906609"""