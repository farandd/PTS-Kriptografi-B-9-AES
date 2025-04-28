# Mini-AES 16-bit Encryption

## Deskripsi
Mini-AES adalah versi sederhana dari algoritma Advanced Encryption Standard (AES) yang dirancang untuk keperluan pembelajaran. Mini-AES mempertahankan struktur dasar AES seperti **SubBytes**, **ShiftRows**, **MixColumns**, dan **AddRoundKey**, namun dengan blok dan kunci berukuran kecil (16-bit).

Project ini memberikan pemahaman praktis tentang bagaimana cipher modern bekerja dalam bentuk sederhana.

---

## Spesifikasi Algoritma

- **Blok**: 16-bit (4 nibble)
- **Kunci**: 16-bit
- **Jumlah Rounds**: 3
- **Operasi Inti**:
  - **SubNibbles**: Substitusi menggunakan S-Box 4-bit.
  - **ShiftRows**: Pergeseran sederhana pada baris.
  - **MixColumns**: Operasi matriks di GF(2⁴).
  - **AddRoundKey**: XOR dengan round key.

- **Key Expansion**: 
  - Berdasarkan operasi sederhana untuk menghasilkan 3 round keys dari key awal 16-bit.

---

## Implementasi

### Fitur Utama
- Enkripsi Mini-AES 16-bit
- Key Expansion untuk menghasilkan round keys
- GUI berbasis **Tkinter**/**Streamlit** (sesuai implementasi)
- Menampilkan output setiap proses round
- Minimal 3 test case untuk validasi hasil
- Dekripsi Mini-AES (opsional tambahan)
- Mode Operasi Blok **ECB** dan **CBC** (opsional tambahan)
- Simpan/Load data dari file TXT/CSV

### Bahasa Pemrograman
- Python

---

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Install Streamlit (jika menggunakan GUI berbasis web):
    ```bash
    pip install streamlit
    ```
3. Jalankan program:
    ```bash
    python mini_aes.py
    ```
   atau jika menggunakan Streamlit:
    ```bash
    streamlit run mini_aes.py
    ```

---

## Flowchart Mini-AES

### Flowchart Enkripsi Mini-AES
```
Start ➔ Input Plaintext dan Key ➔ Key Expansion ➔ 
For each Round:
    - SubNibbles
    - ShiftRows
    - MixColumns (kecuali round terakhir)
    - AddRoundKey
End ➔ Output Ciphertext
```

### Flowchart Key Expansion
```
Start ➔ Input Key ➔ Generate Round Keys ➔ Output Round Keys
```

---

## Test Cases

| No | Plaintext | Key | Ciphertext |
|:---|:----------|:----|:-----------|
| 1  | 0x1234    | 0x5678 | 0x9ABC    |
| 2  | 0xAAAA    | 0x5555 | 0xFFFF    |
| 3  | 0x0000    | 0xFFFF | 0x1357    |

> **Catatan:** Ini hanya contoh. Testcase bisa diubah

---

## Analisis

### Kelebihan Mini-AES
- Struktur mirip AES sehingga cocok untuk pembelajaran.
- Ukuran kecil sehingga lebih mudah dipahami dan di-debug.
- Menunjukkan prinsip penting cipher modern: substitution, permutation, key mixing.

### Keterbatasan Mini-AES
- Blok dan key terlalu kecil untuk keamanan nyata.
- Lebih rentan terhadap brute-force attack.
- Operasi matematis sederhana tidak cukup kompleks untuk aplikasi keamanan serius.

---

## Spesifikasi Tambahan

- **Dekripsi Mini-AES**: 
  - Menggunakan operasi invers (Inverse S-Box, Inverse ShiftRows, Inverse MixColumns).
- **Analisis Avalanche Effect**:
  - Mengamati perubahan ciphertext saat ada perubahan 1-bit pada plaintext/key.
- **Mode Operasi Blok**:
  - ECB dan CBC.
- **Export/Import File**:
  - Menyimpan proses enkripsi/dekripsi ke file TXT/CSV.

---

## Struktur File

```
mini_aes/
├── avalanche_analysis.py     # Analisis efek avalanche (perubahan bit)
├── ecbc.py                   # Implementasi mode operasi blok ECB dan CBC
├── gui.py                    # GUI aplikasi (Tkinter atau Streamlit)
├── mini_aes.py                # Implementasi utama Mini-AES (enkripsi dan dekripsi)
├── mini-aes-encryption.py     # Main program/script utama
├── testcase.py                # Kumpulan test case untuk validasi Mini-AES
├── txtcsv.py                  # Ekspor dan impor input/output ke file TXT atau CSV
└── README.md                  
```
