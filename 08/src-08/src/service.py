from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import Column, CHAR, String


class Sdm(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    npp: str
    nama: str


class Produk(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True
    )

    kode_produk: str = Field(
        sa_column=Column(CHAR(10), nullable=False)
    )

    nama_produk: str = Field(
        sa_column=Column(String(100), nullable=False)
    )

    tersedia: bool

    harga: float


engine = create_engine("sqlite:///departemen-sdm.db")


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()

@app.get("/sdm/", response_model=List[Sdm])
def read_sdm(session: Session = Depends(get_session)):
    # SQLModel select statement
    statement = select(Sdm)
    results = session.exec(statement).all()
    return results

@app.get("/produk/", response_model=List[Produk])
def read_produk(session: Session = Depends(get_session)):
    # SQLModel select statement
    statement = select(Produk)
    results = session.exec(statement).all()
    return results
