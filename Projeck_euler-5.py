#euler 5
#Berapa bilangan positif terkecil yang habis dibagi semua bilangan dari 1 sampai 20?
def inidevisian(angka): # fungsi ini untuk mengecek apakah nilai tersebut dapat dibagi dari 1 sampai 20
    for i in range(1,21): # dengan menggunkan perulangan for
       if angka % i != 0: # dan if berfungsi sebagai pembuktian apakah angka dapat di bagi dari 1 sampai 20
           return False # jika tidak makan akan mengembalikan false
    return True # jika benar maka akan mengembalikan true

angka = 1 
while True: # dengan menggunkan perulangan while akan di cari angka yang dapat di bagi 1 sampai 20
    if inidevisian(angka): # dengan fungsi inidevisian jika mengembalikan nilai true maka loop akan berhenti
        break
    angka += 1 # increment 

print (angka) # print hasil