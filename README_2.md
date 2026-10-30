# Largest Monotonically Increasing Subsequence (LMIS)

## 1. Deskripsi Tugas

Tugas praktikum ini bertujuan untuk mengimplementasikan sebuah program yang dapat menyelesaikan permasalahan **Largest Monotonically Increasing Subsequence (LMIS)** menggunakan bahasa pemrograman Python.

LMIS merupakan permasalahan untuk menemukan subsequence dengan jumlah elemen terbanyak dari suatu urutan bilangan, dengan ketentuan bahwa elemen-elemen tersebut tersusun secara meningkat.

Subsequence tidak harus terdiri dari elemen yang bersebelahan dalam urutan aslinya, tetapi urutan posisi elemen harus tetap dipertahankan.

## 2. Tujuan

- Memahami konsep Largest Monotonically Increasing Subsequence.
- Mengimplementasikan algoritma pencarian subsequence terpanjang.
- Memahami penerapan algoritma dalam penyelesaian permasalahan teori graf dan struktur Tree.
- Menghasilkan program yang fleksibel dan mudah digunakan.

## 3. Contoh Permasalahan

Diberikan urutan bilangan sebagai berikut:

```text
4, 1, 13, 7, 0, 2, 8, 11, 3
```

Program diminta mencari subsequence meningkat dengan jumlah elemen terbanyak.

Salah satu hasil yang memenuhi adalah:

```text
0, 2, 8, 11
```

Dengan panjang subsequence:

```text
4
```

## 4. Algoritma yang Digunakan

Program menggunakan pendekatan **Dynamic Programming dengan Binary Search** untuk menemukan subsequence meningkat terpanjang secara efisien.

Kompleksitas algoritma:

- Time Complexity: O(n log n)
- Space Complexity: O(n)

## 5. Fitur Program

Program menyediakan beberapa fitur:

1. **Example Input** – Menggunakan data contoh yang tersedia pada materi perkuliahan.
2. **Manual Input** – Pengguna dapat memasukkan urutan bilangan sendiri.
3. **Strictly Increasing** – Mencari subsequence dengan setiap elemen berikutnya harus lebih besar.
4. **Non-decreasing** – Mencari subsequence dengan elemen berikutnya boleh sama atau lebih besar.
5. **Subsequence Output** – Menampilkan hasil subsequence terpanjang.
6. **Length Information** – Menampilkan jumlah elemen hasil subsequence.
7. **Index Information** – Menampilkan posisi elemen yang terpilih pada data awal.

## 6. Persyaratan Sistem

- Python 3.x
- Tidak memerlukan library eksternal.
- Menggunakan library bawaan Python.

## 7. Cara Menjalankan Program

1. Pastikan Python 3 sudah terinstal.
2. Simpan source code dengan nama `lmis.py`.
3. Buka terminal atau command prompt pada direktori program.
4. Jalankan perintah berikut:

```bash
python lmis.py
```

5. Pilih menu yang tersedia.
6. Masukkan data bilangan atau gunakan contoh dari materi perkuliahan.

## 8. Contoh Output

```text
Data input       : [4, 1, 13, 7, 0, 2, 8, 11, 3]
Subsequence      : [0, 2, 8, 11]
Panjang LMIS     : 4
Indeks elemen    : [4, 5, 6, 7]
Mode             : strict
```

## 9. Kesimpulan

Program Largest Monotonically Increasing Subsequence (LMIS) dikembangkan untuk menemukan subsequence meningkat terpanjang dari suatu urutan bilangan secara otomatis.

Dengan menggunakan pendekatan Dynamic Programming dan Binary Search, program dapat melakukan pencarian secara efisien serta memberikan informasi hasil yang mudah dipahami oleh pengguna.

---

**Course:** Graph Theory – Tree  
**Assignment:** Practical Assignment 1  
**Topic:** Largest Monotonically Increasing Subsequence  
**Programming Language:** Python 3  
