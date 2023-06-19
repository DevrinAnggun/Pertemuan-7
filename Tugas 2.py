def selection_sort(nama):
    for i in range(len(nama)):
        min_index = i

        for j in range(i + 1, len(nama)):
            if nama[min_index] > nama[j]:
                min_index = j

        nama[j], nama[min_index] = nama[min_index], nama[i]

nama = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", 
        "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]

print(f"Nama 10 Anggota Organisasi ")
print(f"Before : {nama}")
selection_sort(nama)
print(f"After : {nama}")