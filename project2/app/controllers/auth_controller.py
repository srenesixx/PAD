from __future__ import annotations

from app.models.user_model import User, UserModel


class AuthController:
    def __init__(self) -> None:
        self.user_model = UserModel()

    def login(self, username: str, password: str) -> User | None:
        if not username.strip() or not password:
            return None
        return self.user_model.authenticate(username, password)

