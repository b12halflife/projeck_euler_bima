#cari triplet Pythagoras dengan a + b + c = 1000.Cari produk abc.
jumlah = 1000  #angka yang di cari
for a in range(1,jumlah):       #loop mencari angaka yang tepat
    for b in range(1,jumlah-a): #/
        c = jumlah - a -b       #karna a< b< c , c dapat di cari dengan megurangi jumlah-a-b
        if a**2 + b**2 == c**2: #karna a**2 + b**2 = c** 
            print ("terdapat triplet dari",jumlah,"=",a,"+",b,"+",c)
            print (a,"+",b,"=",c,"=",a*b*c)
            break
#by bima