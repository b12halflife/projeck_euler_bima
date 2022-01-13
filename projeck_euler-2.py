"""
Setiap suku baru dalam deret Fibonacci dihasilkan dengan menambahkan dua suku sebelumnya. Dengan memulai dengan 1 dan 2, 10 suku pertama adalah:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Dengan mempertimbangkan suku-suku dalam barisan Fibonacci yang nilainya tidak melebihi empat juta, temukan jumlah suku-suku yang bernilai genap.

"""
limit = 4000000  # batas dari deret fibonaci
a = 2     #
b = 8     # agar lebih cepat kita mengunkan 2,8,34 karna bernilai genap
c = 34    #
sum = 10
while c < limit:
  sum += c  
  a = b
  b = c
  c = 4 * b + a
  print(a,b,c)

print("hasil = ",sum)