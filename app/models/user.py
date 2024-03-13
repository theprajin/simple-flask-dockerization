from dataclasses import dataclass

from app import db


@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), nullable=False)
    email: str = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return f"user is {self.name}"
