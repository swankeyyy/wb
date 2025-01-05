from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class Article(IdPkMixin, Base):
    __tablename__ = "articles"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    article: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    category: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<Article(name={self.name} - {self.article})>"
