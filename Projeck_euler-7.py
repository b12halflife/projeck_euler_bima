# Mencari bilangan prima pada angka yang di cari

def ini_prima(angka): # Memastikan angka adalah prima
    if angka < 2: # mencek angka adalah bukan prima dan komposit
        return "Bukan prima / angka komposit"
    for i in range(2,int(angka**0.5)+1):# memastikan angka adalah prima
        if angka % i == 0:
            return False
    return True

def nthprima (angka): # Mengembalikan nilai prima 
    bil_prima = 0
    ang_prima = 1
    while bil_prima < angka :
        ang_prima += 1
        if ini_prima(ang_prima):
            bil_prima += 1
    return ang_prima
            
print(nthprima(10001)) #