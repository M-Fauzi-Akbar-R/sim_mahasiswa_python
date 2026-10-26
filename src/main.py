from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from src.models import Mahasiswa, DaftarMahasiswa

console = Console()
db = DaftarMahasiswa()


def tampilkan_menu():
    menu_text = (
        "[bold cyan]Sistem Informasi Mahasiswa[/]\n\n"
        "1. Tambah Mahasiswa\n"
        "2. Tampilkan Semua Mahasiswa\n"
        "3. Cari Mahasiswa (NIM)\n"
        "4. Hapus Mahasiswa\n"
        "5. Edit IPK Mahasiswa\n"
        "0. Keluar"
    )
    console.print(Panel(menu_text, title="Menu", border_style="cyan"))


def tambah_mahasiswa():
    console.print("\n[bold]Tambah Mahasiswa Baru[/]")
    try:
        nim = console.input("NIM: ").strip()
        nama = console.input("Nama: ").strip()
        prodi = console.input("Program Studi: ").strip()
        angkatan = int(console.input("Angkatan: "))
        ipk = float(console.input("IPK (0.0-4.0): "))
        mhs = Mahasiswa(nim, nama, prodi, angkatan, ipk)
        db.tambah(mhs)
        console.print(f"[green]Berhasil: {nama} ditambahkan[/]")
    except ValueError as e:
        console.print(f"[red]Gagal: {e}[/]")


def tampilkan_semua():
    if not db.data:
        console.print("[yellow]Belum ada data mahasiswa.[/]")
        return
    table = Table(title="Daftar Mahasiswa")
    table.add_column("NIM", style="cyan")
    table.add_column("Nama")
    table.add_column("Program Studi")
    table.add_column("Angkatan", justify="right")
    table.add_column("IPK", justify="right")
    for m in db.data:
        table.add_row(m.nim, m.nama, m.program_studi, str(m.angkatan), f"{m.ipk:.2f}")
    console.print(table)


def cari_mahasiswa():
    nim = console.input("Masukkan NIM yang dicari: ").strip()
    mhs = db.cari(nim)
    if mhs:
        console.print(f"[green]Data ditemukan:[/] {mhs}")
    else:
        console.print("[yellow]Mahasiswa dengan NIM tersebut tidak ditemukan.[/]")


def hapus_mahasiswa():
    nim = console.input("Masukkan NIM yang akan dihapus: ").strip()
    if db.hapus(nim):
        console.print("[green]Data mahasiswa berhasil dihapus.[/]")
    else:
        console.print("[yellow]NIM tidak ditemukan; tidak ada data yang dihapus.[/]")


def edit_ipk():
    nim = console.input("Masukkan NIM mahasiswa: ").strip()
    mhs = db.cari(nim)
    if not mhs:
        console.print("[yellow]NIM tidak ditemukan.[/]")
        return
    try:
        ipk_baru = float(console.input("Masukkan IPK baru (0.0-4.0): "))
        if db.edit_ipk(nim, ipk_baru):
            console.print("[green]IPK berhasil diperbarui.[/]")
    except ValueError as e:
        console.print(f"[red]Gagal: {e}[/]")


def main():
    while True:
        tampilkan_menu()
        pilihan = console.input("\nPilih [0-5]: ").strip()
        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            edit_ipk()
        elif pilihan == "0":
            console.print("[bold]Sampai jumpa![/]")
            break
        else:
            console.print("[red]Pilihan tidak valid.[/]")


if __name__ == "__main__":
    main()
