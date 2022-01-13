#projeck euler 3 Mencari bilangan prima terbesar dari 600851475143 

angka=13195 # nominal
i=2 # pembagi terkecil 2
for k in range(0,angka):
    if i >= angka: #Faktor prima dari bilangan tersebut tidak boleh lebih besar dari bilangan tersebut
        break
    elif angka % i == 0: # mengecek bilangan habis di bagi i
        angka = angka / i
    else:
        i= i + 1 # jika tidak habis di bagi i maka i =3

print ("bilangan prima terbesar adalah: ",angka)   