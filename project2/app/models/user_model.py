from __future__ import annotations

from dataclasses import dataclass

from app.database import fetch_one


@dataclass(frozen=True)
class User:
    id: int
    username: str
    role: str
    nama: str


class UserModel:
    """Access user records stored in SQLite."""

    SELECT_USER = """
        SELECT id, username, role, nama
        FROM users
        WHERE username = ? AND password = ?
        LIMIT 1
    """
    SELECT_BY_ID = """
        SELECT id, username, role, nama
        FROM users
        WHERE id = ?
        LIMIT 1
    """

    @staticmethod
    def _to_user(row) -> User:
        return User(
            id=row["id"],
            username=row["username"],
            role=row["role"],
            nama=row["nama"],
        )

    def authenticate(self, username: str, password: str) -> User | None:
        row = fetch_one(self.SELECT_USER, (username.strip(), password))
        return self._to_user(row) if row is not None else None

    def get_by_id(self, user_id: int) -> User | None:
        row = fetch_one(self.SELECT_BY_ID, (user_id,))
        return self._to_user(row) if row is not None else None
