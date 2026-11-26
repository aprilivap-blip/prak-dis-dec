from sqlmodel import Session, select, SQLModel
from service import engine, Produk

# Membuat tabel berdasarkan model yang tersedia
SQLModel.metadata.create_all(engine)

# Data produk yang akan dimasukkan
data_produk = [
    Produk(
        kode_produk="PRD001",
        nama_produk="Laptop",
        tersedia=True,
        harga=7500000.50
    ),
    Produk(
        kode_produk="PRD002",
        nama_produk="Mouse",
        tersedia=True,
        harga=150000.00
    ),
    Produk(
        kode_produk="PRD003",
        nama_produk="Keyboard",
        tersedia=True,
        harga=275000.50
    ),
    Produk(
        kode_produk="PRD004",
        nama_produk="Monitor",
        tersedia=False,
        harga=1850000.00
    ),
    Produk(
        kode_produk="PRD005",
        nama_produk="Flashdisk",
        tersedia=True,
        harga=85000.75
    )
]

# Memasukkan data ke database
with Session(engine) as session:
    data_lama = session.exec(select(Produk)).all()

    if not data_lama:
        session.add_all(data_produk)
        session.commit()
        print("5 data produk berhasil dimasukkan.")
    else:
        print("Data produk sudah tersedia.")