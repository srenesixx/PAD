from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from app.database import get_connection


@dataclass(frozen=True)
class User:
    id: int
    username: str
    role: str
    nama: str


class UserModel:
    """Access user records stored in SQLite."""

    def authenticate(self, username: str, password: str) -> Optional[User]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, username, role, nama
            FROM users
            WHERE username = ? AND password = ?
            LIMIT 1
            """,
            (username.strip(), password),
        )
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None

        return User(
            id=row["id"],
            username=row["username"],
            role=row["role"],
            nama=row["nama"],
        )

    def get_by_id(self, user_id: int) -> Optional[User]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, username, role, nama
            FROM users
            WHERE id = ?
            LIMIT 1
            """,
            (user_id,),
        )
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None

        return User(
            id=row["id"],
            username=row["username"],
            role=row["role"],
            nama=row["nama"],
        )

