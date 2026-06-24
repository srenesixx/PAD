from __future__ import annotations

"""Compatibility imports for older entry points."""

from app.database import (
    DB_PATH,
    ensure_database,
    execute,
    fetch_all,
    fetch_one,
    get_connection,
    init_database,
    insert_default_data,
)

__all__ = [
    "DB_PATH",
    "ensure_database",
    "execute",
    "fetch_all",
    "fetch_one",
    "get_connection",
    "init_database",
    "insert_default_data",
]
