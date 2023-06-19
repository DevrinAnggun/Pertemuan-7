def bubble_sort(ips):
    for i in range(len(ips)):
        for j in range(len(ips) - i - 1):
            if ips[j] < ips[j + 1]:
                ips[j], ips[j + 1] = ips[j + 1], ips[j]

    return ips

ips_mahasiswa= [3.8, 2.9, 3.3, 4.0, 2.4]

print(f"Indeks Prestasi Semester (IPS) ")
print(f"List sebelum diurutkan : {ips_mahasiswa}")
bubble_sort(ips_mahasiswa)
print(f"List setelah diurutkan : {ips_mahasiswa}")
print(" ")