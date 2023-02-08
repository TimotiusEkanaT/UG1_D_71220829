print ("==================== KASIR ====================")

fuuuu = 0
while True:
    bahbab = int(input("Harga Barang : "))
    cascad = input ("Apakah anda membeli barang lagi? [yes/no] :")
    if cascad == ("yes"):
        fuuuu += bahbab
    else: 
        print ("TOTAL BELANJA : ", fuuuu+0)
        break

