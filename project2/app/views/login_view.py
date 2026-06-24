from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from app.theme import STYLES


class LoginView(ttk.Frame):
    def __init__(self, master, on_login) -> None:
        super().__init__(master, padding=0)
        self.on_login = on_login
        self.configure(style=STYLES["root"])
        self._build()

    def _build(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        backdrop = ttk.Frame(self, style=STYLES["login_backdrop"])
        backdrop.grid(row=0, column=0, sticky="nsew")
        backdrop.columnconfigure(0, weight=1)
        backdrop.columnconfigure(1, weight=0, minsize=460)
        backdrop.columnconfigure(2, weight=1)
        backdrop.rowconfigure(0, weight=1)
        backdrop.rowconfigure(1, weight=0)
        backdrop.rowconfigure(2, weight=1)

        shell = ttk.Frame(backdrop, style=STYLES["login_card"], padding=(36, 38))
        shell.grid(row=1, column=1, sticky="nsew")
        shell.columnconfigure(0, weight=1)

        header = ttk.Frame(shell, style=STYLES["login_card"])
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)

        ttk.Label(header, text="Sistem Absensi", style=STYLES["login_title"]).grid(row=0, column=0, sticky="w")

        divider = ttk.Separator(shell, orient="horizontal")
        divider.grid(row=1, column=0, sticky="ew", pady=(18, 22))

        form = ttk.Frame(shell, style=STYLES["login_card"])
        form.grid(row=2, column=0, sticky="nsew")
        form.columnconfigure(0, weight=1)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.message_var = tk.StringVar()

        self.username_entry = self._add_field(form, 0, "Username", self.username_var)
        self.password_entry = self._add_field(form, 2, "Password", self.password_var, show="*")

        self.login_button = ttk.Button(form, text="Masuk", command=self._submit, style=STYLES["button_primary"])
        self.login_button.grid(row=4, column=0, sticky="ew", pady=(10, 0))

        self.message_label = ttk.Label(form, textvariable=self.message_var, style=STYLES["login_message"], wraplength=360, justify="left")
        self.message_label.grid(row=5, column=0, sticky="w", pady=(16, 0))

        self.username_entry.focus_set()
        self.username_entry.bind("<Return>", self._focus_password)
        self.password_entry.bind("<Return>", self._submit_event)

    def _add_field(self, parent, row: int, label: str, variable: tk.StringVar, show: str | None = None) -> ttk.Entry:
        ttk.Label(parent, text=label, style=STYLES["form_label"]).grid(row=row, column=0, sticky="w", pady=(0, 7))
        entry = ttk.Entry(parent, textvariable=variable, style=STYLES["form_entry"], show=show or "")
        entry.grid(row=row + 1, column=0, sticky="ew")
        return entry

    def _focus_password(self, event=None) -> None:
        self.password_entry.focus_set()

    def _submit_event(self, event=None) -> None:
        self._submit()

    def _submit(self) -> None:
        self.message_var.set("")
        self.on_login(self.username_var.get(), self.password_var.get())

    def show_error(self, message: str) -> None:
        self.message_var.set(message)

    def clear(self) -> None:
        self.username_var.set("")
        self.password_var.set("")
        self.message_var.set("")
        self.username_entry.focus_set()
