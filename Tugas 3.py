input_buku = []
def addBuku():
    jumlah = int(input("\nMasukkan Total Buku : "))
    for i in range(jumlah):
        judul_buku = input(f"Masukkan Judul Buku Ke-{i + 1} : ")
        input_buku.append(judul_buku)
        jumlah = jumlah - 1

        while(True):
            jumlah = jumlah - 1
            if(jumlah<0):
                break

def asc(arraybuku):
    for i in range(1, len(arraybuku)):
        item = arraybuku[i]
        j = i - 1

        while j >=0 and arraybuku[j] > item:
            arraybuku[j + 1] = arraybuku[j]
            j -= 1

        arraybuku[j + 1] = item

    print("\nSorting Buku Secara Ascending")
    print(" ")
    for x in range(len(arraybuku)):
        print (f"Judul Buku ke-(x + 1)) : %s" %arraybuku[x] )
        print(" ")
        return arraybuku
    
def desc(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j>=0 and array[j] < item:
            array[j + 1] = item
            j -= 1

    print("\nSorting Buku Secara Descending")
    print(" ")
    for x in range(len(array)):
        print (f"Judul Buku Ke-{x + 1} : %s" %array[x] )
    print(" ")

    return array

addBuku()
print("\n<======== Urutkan? ========>")
print("1. Insertion Ascending ")
print("2. Insertion Descending ")

pilih = int(input("Pilih: "))
if (pilih == 1):
    asc(input_buku)
elif (pilih == 2):
    desc(input_buku)
else:
    print("\nPilihan tidak ada")