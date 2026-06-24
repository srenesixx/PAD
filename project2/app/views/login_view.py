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

        card = ttk.Frame(backdrop, style=STYLES["login_card"], padding=(36, 34))
        card.grid(row=1, column=1, sticky="nsew")
        card.columnconfigure(0, weight=1)

        title = ttk.Label(
            card,
            text="Sistem Absensi",
            style=STYLES["login_title"],
        )
        title.grid(row=0, column=0, pady=(2, 6), sticky="w")

        subtitle = ttk.Label(
            card,
            text="Masuk untuk mengelola absensi",
            style=STYLES["login_subtitle"],
        )
        subtitle.grid(row=1, column=0, pady=(0, 24), sticky="w")

        form = ttk.Frame(card, style=STYLES["login_card"])
        form.grid(row=2, column=0, padx=36, sticky="nsew")
        form.columnconfigure(0, weight=1)

        ttk.Label(form, text="Username", style=STYLES["form_label"]).grid(row=0, column=0, sticky="w", pady=(0, 7))
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(form, textvariable=self.username_var, style=STYLES["form_entry"])
        self.username_entry.grid(row=1, column=0, sticky="ew", pady=(0, 16), ipady=5)

        ttk.Label(form, text="Password", style=STYLES["form_label"]).grid(row=2, column=0, sticky="w", pady=(0, 7))
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(form, textvariable=self.password_var, show="*", style=STYLES["form_entry"])
        self.password_entry.grid(row=3, column=0, sticky="ew", pady=(0, 22), ipady=5)

        self.login_button = ttk.Button(form, text="Masuk", command=self._submit, style=STYLES["button_primary"])
        self.login_button.grid(row=4, column=0, sticky="ew")

        hint = ttk.Label(
            card,
            text="Default: dosen1 / 123456 atau mahasiswa1 / 123456",
            style=STYLES["login_hint"],
        )
        hint.grid(row=5, column=0, pady=(28, 0), sticky="w")

        self.message_var = tk.StringVar()
        message = ttk.Label(
            card,
            textvariable=self.message_var,
            style=STYLES["login_message"],
        )
        message.grid(row=6, column=0, pady=(12, 0), sticky="w")

        self.username_entry.focus_set()
        self.username_entry.bind("<Return>", self._focus_password)
        self.password_entry.bind("<Return>", self._submit_event)

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
