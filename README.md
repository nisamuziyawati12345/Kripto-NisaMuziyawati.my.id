# 🔐 Tugas1_Kriptografi

Aplikasi web kriptografi berbasis Flask yang mendukung beberapa algoritma cipher klasik seperti Caesar Cipher, Vigenere Cipher, Affine Cipher, Playfair Cipher, dan Hill Cipher.

Project ini dibuat untuk memenuhi tugas mata kuliah Kriptografi dengan fitur visualisasi proses enkripsi dan dekripsi secara interaktif.

---

# 📚 Algoritma yang Digunakan

## 1. Caesar Cipher
Metode kriptografi klasik dengan pergeseran huruf berdasarkan key tertentu.

### Rumus
```text
C = (P + K) mod 26
```

---

## 2. Vigenere Cipher
Menggunakan kombinasi plaintext dan key berbentuk huruf.

### Rumus
```text
Ci = (Pi + Ki) mod 26
```

---

## 3. Affine Cipher
Menggunakan fungsi matematika linear.

### Rumus
```text
C = (aP + b) mod 26
```

---

## 4. Playfair Cipher
Menggunakan matrix 5x5 dan pasangan huruf.

### Rule
- Same Row
- Same Column
- Rectangle Rule

### Fitur
- Visualisasi Matrix Playfair 5x5
- Tampilan grid responsive
- Detail langkah perhitungan

---

## 5. Hill Cipher
Menggunakan operasi perkalian matriks.

### Rumus
```text
C = K × P mod 26
```

---

# 🛠️ Teknologi

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- Jinja2

---

# 📂 Struktur Project

```text
Tugas1_Kriptografi/
│
├── algorithms/
│   ├── affine.py
│   ├── caesar.py
│   ├── hill.py
│   ├── playfair.py
│   └── vigenere.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
│
├── venv/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ✨ Fitur Utama

- Enkripsi dan Dekripsi
- Tampilan modern dark mode
- Responsive mobile
- Visualisasi langkah perhitungan
- Visualisasi Matrix Playfair
- Penjelasan algoritma
- Tabel hasil proses cipher

---

# ▶️ Cara Menjalankan Project

## 1. Clone Project

```bash
git clone <repository-url>
```

---

## 2. Masuk Folder Project

```bash
cd Tugas1_Kriptografi
```

---

## 3. Aktifkan Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependency

```bash
pip install flask
```

atau

```bash
pip install -r requirements.txt
```

---

## 5. Jalankan Flask

```bash
python app.py
```

atau

```bash
flask run
```

---

## 6. Buka Browser

```text
http://127.0.0.1:5000
```

---

# 📸 Tampilan Aplikasi

## Halaman Input
- Pilih algoritma
- Input plaintext / ciphertext
- Input key
- Pilih encrypt atau decrypt

## Halaman Result
- Hasil enkripsi/dekripsi
- Formula algoritma
- Langkah perhitungan
- Matrix Playfair 5x5
- Visualisasi tabel proses

---

# 📱 Responsive Design

Aplikasi mendukung:
- Desktop
- Tablet
- Mobile

---

# 👨‍💻 Developer

Nama : Nisa Muziyawati  
NIM : 301230045  
Kelas : IF 5B  
Program Studi : Teknik Informatika

---

# 📖 Mata Kuliah

Kriptografi

---

# ✅ Status Project

Project selesai dengan fitur:
- Caesar Cipher
- Vigenere Cipher
- Affine Cipher
- Playfair Cipher
- Hill Cipher
- Visualisasi matriks
- UI modern responsive
```