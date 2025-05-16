from sqlalchemy import MetaData, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_N_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        },
    )

    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(String(200), index=True)
    login: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(200))
