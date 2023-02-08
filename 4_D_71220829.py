print ("--------Nilai ke 1 --------")
harianto = int(input("Nilai harian : "))
utis = int(input("Nilai UTS : "))
uasd = int(input("Nilai UAS : "))
print ("--------Nilai ke 2 --------")
haria = int(input("Nilai harian : "))
utisa = int(input("Nilai UTS : "))
uasda = int(input("Nilai UAS : "))
print ("--------Total Nilai --------")
pasda = ((((harianto*30/100)) + (utis*30/100) + (uasd*40/100) + (haria*30/100) + (utisa*30/100) + (uasda*40/100))/6)
print ("Total nilai yang didapat :",pasda)

if pasda < 20:
    print ("Total nilai yang didapat dalam huruf : E")
elif pasda < 40:
    print ("Total nilai yang didapat dalam huruf : D")
elif pasda < 60:
    print ("Total nilai yang didapat dalam huruf : C")
elif pasda < 80:
    print ("Total nilai yang didapat dalam huruf : B")
else:
    print ("Total nilai yang didapat dalam huruf : A")