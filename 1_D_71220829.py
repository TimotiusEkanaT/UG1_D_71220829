print ("==================== KASIR ====================")
bahbab = int(input("Harga Barang : "))
bahhe = bahbab
while True:
    cascad = input ("Apakah anda membeli barang lagi? [yes/no] :")
    if cascad == ("yes"):
        print (bahhe)
        bahhe = bahbab + bahhe
    else: 
        break
