#Tambah Data Mhs
def addMahasiswa():
    jumlah = int(input("Jumlah mahasiswa: "))
    mahasiswa = []
    while(jumlah > 0):
        nama = input("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1

    while(True):
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if(jumlah<0):
            break

#Hapus Data Mhs
def removeMahasiswa(arrayMahasiswa):
        mahasiswa = arrayMahasiswa
        print("Data mahasiswa %s" %arrayMahasiswa)
        mahasiswa.remove(input("Hapus mahasiswa: "))
        print("Data mahasiswa %s" %mahasiswa)
        panggil(mahasiswa)
        
#Urutkan Data Mhs
def ascMahasiswa(arrayMahasiswa):
        mahasiswa = arrayMahasiswa
        mahasiswa.sort()
        print(mahasiswa)
        panggil(mahasiswa)

#Lihat Data Mhs
def viewMahasiswa(arrayMahasiswa):
        mahasiswa = arrayMahasiswa
        for x in mahasiswa:
            print("Nama Mahasiswa: %s" %x)
        panggil(arrayMahasiswa)

#Menu
def panggil(arrayMahasiswa):
        print("\n<======== Menu Data Mahasiswa ========>")
        print("1. Tambah Data Mahasiswa ")
        print("2. Hapus Data Mahasiswa ")
        print("3. Urutkan Data Mahasiswa ")
        print("4. Lihat Data Mahasiswa")
        print("5. Tutup ")

        pilih = int(input("Pilih: "))
        if(pilih==1):
            addMahasiswa()
        elif(pilih==2):
            removeMahasiswa(arrayMahasiswa)
        elif(pilih==3):
            ascMahasiswa(arrayMahasiswa)
        elif(pilih==4):
            viewMahasiswa(arrayMahasiswa)
        else:
            print("Selesai")

addMahasiswa()