buddi = eval(input("Masukkan Angka: "))

for assdi in range(buddi):
    print(" " * (buddi - assdi), "*" * (2*assdi + 1))
for assdi in range(buddi - 2, -1, -1):
    print(" " * (buddi - assdi), "*" * (2*assdi + 1))