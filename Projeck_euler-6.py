#euler 6
#Temukan perbedaan antara jumlah kuadrat dari seratus bilangan asli pertama dan kuadrat dari jumlah tersebut.
a,b = 0,0
x,y = 0,0
for i in range(101):#jumlah dari seratus bilangan asli pertama
    x=i*i
    a=x+a
print("jumlah penambahan dari seratus bilangan asli pertama = ",a)
for i in range(101):#kuadrat dari seratus bilangan asli pertama
    b = i+b
    y = b*b
print("jumlah kuadrat dari seratus bilangan asli pertama = ",y)    
hasil = y - a # perbedaan antara jumlah kuadrat dari seratus bilangan asli pertama dan kuadrat dari jumlah
print(y,"-",a,"=",hasil)
