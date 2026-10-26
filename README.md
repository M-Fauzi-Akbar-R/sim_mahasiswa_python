# Sistem Informasi Mahasiswa (SIM)

Aplikasi console-based untuk mengelola data mahasiswa pada Program Studi Sistem Informasi.

## Identitas
- Nama: Muhammad Fauzi Akbar Rafsanjani
- NIM: 20241320022
- Kelas: A1-Sistem Informasi

## Fitur
- Tambah data mahasiswa (NIM, nama, program studi, angkatan, IPK)
- Tampilkan seluruh data dalam tabel
- Cari mahasiswa berdasarkan NIM
- Hapus data mahasiswa
- Edit IPK mahasiswa dengan validasi 0.0-4.0
- Validasi NIM, nama, IPK, dan NIM duplikat

## Prasyarat
- Python 3.10 atau lebih baru
- pip

## Instalasi (Windows / VS Code)
```powershell
py -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Jika PowerShell menolak aktivasi, jalankan di Command Prompt:
```bat
venv\Scripts\activate.bat
```

## Menjalankan program
```powershell
python -m src.main
```

## Pengujian
```powershell
python -m pytest tests/ -v
```

## Struktur Proyek
- `src/models.py` — model dan operasi data mahasiswa
- `src/main.py` — program utama dan menu interaktif
- `tests/test_main.py` — unit test
- `docs/` — tempat screenshot output program

## Setup Checklist
- [x] Python 3.10+ terinstal (versi: 3.14.8)
- [x] pip terinstal dan berfungsi
- [x] Virtual environment dibuat dan diaktivasi
- [x] Paket terinstal melalui requirements.txt
- [x] Program berjalan tanpa error
- [x] Unit test lulus
- [x] Repositori Git diinisiasi
- [x] Remote GitHub terhubung
- [x] Push ke GitHub berhasil
- [x] README.md lengkap
- [x] Minimal 3 commit bermakna
- [x] Screenshot output disimpan di `docs/`
