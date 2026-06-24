from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from app.theme import COLORS, STYLES


class DashboardView(ttk.Frame):
    def __init__(
        self,
        master,
        user,
        summary: dict,
        records: list[dict],
        on_check_in,
        on_check_out,
        on_refresh,
        on_logout,
    ) -> None:
        super().__init__(master, padding=0)
        self.user = user
        self.summary = summary
        self.records = records
        self.on_check_in = on_check_in
        self.on_check_out = on_check_out
        self.on_refresh = on_refresh
        self.on_logout = on_logout
        self.configure(style=STYLES["root"])
        self._build()

    def _build(self) -> None:
        self.pack_propagate(False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header = ttk.Frame(self, style=STYLES["header"], padding=(28, 20))
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)

        title = ttk.Label(
            header,
            text=f"Selamat datang, {self.user.nama}",
            style=STYLES["dashboard_title"],
        )
        title.grid(row=0, column=0, sticky="w")

        meta = ttk.Label(
            header,
            text=f"{self.user.role.title()}  |  @{self.user.username}",
            style=STYLES["meta"],
        )
        meta.grid(row=1, column=0, sticky="w", pady=(4, 0))

        logout_button = ttk.Button(header, text="Logout", command=self.on_logout, style=STYLES["button_secondary"])
        logout_button.grid(row=0, column=1, rowspan=2, sticky="e")

        content = ttk.Frame(self, style=STYLES["page"], padding=(24, 24))
        content.grid(row=1, column=0, sticky="nsew")
        content.columnconfigure(0, weight=0, minsize=300)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(1, weight=1)

        self.side_panel = ttk.Frame(content, style=STYLES["panel_dark"], padding=(20, 20), width=330)
        self.side_panel.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=(0, 18))
        self.side_panel.grid_propagate(False)
        self.side_panel.columnconfigure(0, weight=1)

        side_title = ttk.Label(
            self.side_panel,
            text="Aksi Absensi",
            style=STYLES["section_title"],
        )
        side_title.grid(row=0, column=0, sticky="w")

        ttk.Label(self.side_panel, text="Status", style=STYLES["panel_label"]).grid(row=1, column=0, sticky="w", pady=(18, 6))
        self.status_var = tk.StringVar(value="hadir")
        self.status_combo = ttk.Combobox(
            self.side_panel,
            textvariable=self.status_var,
            values=["hadir", "izin", "sakit", "alpha"],
            state="readonly",
            style=STYLES["form_combo"],
        )
        self.status_combo.grid(row=2, column=0, sticky="ew")

        ttk.Label(self.side_panel, text="Keterangan", style=STYLES["panel_label"]).grid(row=3, column=0, sticky="w", pady=(18, 6))
        self.keterangan_text = tk.Text(
            self.side_panel,
            height=5,
            width=30,
            wrap="word",
            bg=COLORS["surface_bg"],
            fg=COLORS["text"],
            insertbackground=COLORS["text"],
            relief="flat",
            highlightthickness=1,
            highlightbackground=COLORS["border_dark"],
            highlightcolor=COLORS["accent"],
            padx=10,
            pady=10,
        )
        self.keterangan_text.grid(row=4, column=0, sticky="ew")

        button_row = ttk.Frame(self.side_panel, style=STYLES["panel_dark"])
        button_row.grid(row=5, column=0, sticky="ew", pady=(16, 0))
        button_row.columnconfigure(0, weight=1)
        button_row.columnconfigure(1, weight=1)

        checkin_button = ttk.Button(button_row, text="Check In", command=self._check_in, style=STYLES["button_primary"])
        checkin_button.grid(row=0, column=0, sticky="ew", padx=(0, 6))

        checkout_button = ttk.Button(button_row, text="Check Out", command=self._check_out, style=STYLES["button_secondary"])
        checkout_button.grid(row=0, column=1, sticky="ew", padx=(6, 0))

        refresh_button = ttk.Button(self.side_panel, text="Refresh", command=self.on_refresh, style=STYLES["button_secondary"])
        refresh_button.grid(row=6, column=0, sticky="ew", pady=(14, 0))

        self.message_var = tk.StringVar()
        self.message_label = ttk.Label(
            self.side_panel,
            textvariable=self.message_var,
            style=STYLES["panel_message"],
            wraplength=270,
            justify="left",
        )
        self.message_label.grid(row=7, column=0, sticky="w", pady=(16, 0))

        self.summary_frame = ttk.Frame(content, style=STYLES["page"])
        self.summary_frame.grid(row=0, column=1, sticky="ew")
        self.summary_frame.columnconfigure(0, weight=1)
        self.summary_frame.columnconfigure(1, weight=1)
        self.summary_frame.columnconfigure(2, weight=1)

        self.card_1 = self._create_card(self.summary_frame, 0)
        self.card_2 = self._create_card(self.summary_frame, 1)
        self.card_3 = self._create_card(self.summary_frame, 2)
        self._render_summary(self.summary)

        table_frame = ttk.Frame(content, style=STYLES["surface"], padding=(16, 16))
        table_frame.grid(row=1, column=1, sticky="nsew", pady=(18, 0))
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(1, weight=1)

        table_title = ttk.Label(
            table_frame,
            text="Riwayat Absensi",
            style=STYLES["table_title"],
        )
        table_title.grid(row=0, column=0, sticky="w", pady=(0, 10))

        columns = ("nama", "tanggal", "masuk", "pulang", "status", "keterangan")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=14)
        headings = {
            "nama": "Nama",
            "tanggal": "Tanggal",
            "masuk": "Masuk",
            "pulang": "Pulang",
            "status": "Status",
            "keterangan": "Keterangan",
        }
        widths = {"nama": 170, "tanggal": 110, "masuk": 90, "pulang": 90, "status": 90, "keterangan": 240}
        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="w")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        self._render_records(self.records)

    def _create_card(self, parent, index: int) -> tk.Frame:
        card = ttk.Frame(parent, style=STYLES["card"], padding=(18, 18))
        card.grid(row=0, column=index, sticky="ew", padx=(0 if index == 0 else 10, 10 if index < 2 else 0))
        card.columnconfigure(0, weight=1)
        label = ttk.Label(card, text="", style=STYLES["card_label"])
        label.grid(row=0, column=0, sticky="w")
        value = ttk.Label(card, text="", style=STYLES["card_value"])
        value.grid(row=1, column=0, sticky="w", pady=(5, 0))
        setattr(self, f"card_{index + 1}_label", label)
        setattr(self, f"card_{index + 1}_value", value)
        return card

    def _render_summary(self, summary: dict) -> None:
        self.card_1_label.config(text=summary.get("label_1", ""))
        self.card_1_value.config(text=str(summary.get("value_1", "-")))
        self.card_2_label.config(text=summary.get("label_2", ""))
        self.card_2_value.config(text=str(summary.get("value_2", "-")))
        self.card_3_label.config(text=summary.get("label_3", ""))
        self.card_3_value.config(text=str(summary.get("value_3", "-")))

    def _render_records(self, records: list[dict]) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)

        for record in records:
            self.tree.insert(
                "",
                "end",
                values=(
                    record.get("nama", "-"),
                    record.get("tanggal", "-"),
                    record.get("jam_masuk") or "-",
                    record.get("jam_pulang") or "-",
                    record.get("status") or "-",
                    record.get("keterangan") or "-",
                ),
            )

    def update_data(self, summary: dict, records: list[dict]) -> None:
        self.summary = summary
        self.records = records
        self._render_summary(summary)
        self._render_records(records)

    def set_message(self, text: str, color: str = "#38bdf8") -> None:
        self.message_var.set(text)
        self.message_label.config(style=STYLES["panel_message"], foreground=color)

    def clear_form(self) -> None:
        self.status_var.set("hadir")
        self.keterangan_text.delete("1.0", "end")
        self.message_label.config(style=STYLES["panel_message"])

    def _check_in(self) -> None:
        self.on_check_in(self.status_var.get(), self.keterangan_text.get("1.0", "end").strip())

    def _check_out(self) -> None:
        self.on_check_out()
