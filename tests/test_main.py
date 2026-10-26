import pytest
from src.models import Mahasiswa, DaftarMahasiswa


def data_contoh():
    return Mahasiswa("2024SI001", "Andi Pratama", "Sistem Informasi", 2024, 3.5)


def test_buat_mahasiswa_valid():
    mhs = data_contoh()
    assert mhs.nim == "2024SI001"
    assert mhs.ipk == 3.5


def test_nim_tidak_valid():
    with pytest.raises(ValueError):
        Mahasiswa("abc", "Test", "SI", 2024, 3.0)


def test_ipk_di_luar_range():
    with pytest.raises(ValueError):
        Mahasiswa("2024SI002", "Test", "SI", 2024, 5.0)


def test_tambah_dan_cari():
    db = DaftarMahasiswa()
    mhs = data_contoh()
    db.tambah(mhs)
    assert db.cari(mhs.nim) == mhs
    assert db.jumlah == 1


def test_nim_duplikat():
    db = DaftarMahasiswa()
    db.tambah(data_contoh())
    with pytest.raises(ValueError):
        db.tambah(Mahasiswa("2024SI001", "Budi", "SI", 2024, 3.0))


def test_nim_kosong():
    with pytest.raises(ValueError):
        Mahasiswa("", "Test", "SI", 2024, 3.0)


def test_nama_sangat_panjang():
    nama = "A" * 300
    mhs = Mahasiswa("2024SI003", nama, "SI", 2024, 3.0)
    assert mhs.nama == nama


@pytest.mark.parametrize("ipk", [0.0, 4.0])
def test_ipk_boundary(ipk):
    mhs = Mahasiswa("2024SI004", "Test", "SI", 2024, ipk)
    assert mhs.ipk == ipk


def test_hapus_nim_tidak_ada():
    db = DaftarMahasiswa()
    assert db.hapus("2024SI999") is False


def test_cari_nim_tidak_ada():
    db = DaftarMahasiswa()
    assert db.cari("2024SI999") is None


def test_edit_ipk():
    db = DaftarMahasiswa()
    db.tambah(data_contoh())
    assert db.edit_ipk("2024SI001", 4.0) is True
    assert db.cari("2024SI001").ipk == 4.0


def test_edit_ipk_tidak_valid():
    db = DaftarMahasiswa()
    db.tambah(data_contoh())
    with pytest.raises(ValueError):
        db.edit_ipk("2024SI001", 4.5)
