from __future__ import annotations

import tkinter as tk

from app.controllers.app_controller import AppController
from app.database import ensure_database


def main() -> None:
    ensure_database()
    root = tk.Tk()
    AppController(root)
    root.mainloop()


if __name__ == "__main__":
    main()

