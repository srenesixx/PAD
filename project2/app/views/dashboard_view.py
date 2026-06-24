from __future__ import annotations

from datetime import date
import tkinter as tk
from tkinter import ttk

from app.theme import COLORS, STYLES


class DashboardView(ttk.Frame):
    STATUS_OPTIONS = ("hadir", "izin", "sakit", "alpha")
    COLUMNS = ("nama", "tanggal", "masuk", "pulang", "status", "keterangan")
    HEADINGS = {
        "nama": "Nama",
        "tanggal": "Tanggal",
        "masuk": "Masuk",
        "pulang": "Pulang",
        "status": "Status",
        "keterangan": "Keterangan",
    }
    WIDTHS = {"nama": 180, "tanggal": 110, "masuk": 90, "pulang": 90, "status": 90, "keterangan": 260}

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
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._build_header()
        self._build_content()

    def _build_header(self) -> None:
        header = ttk.Frame(self, style=STYLES["header"], padding=(28, 22))
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)
        header.columnconfigure(1, weight=0)

        title_box = ttk.Frame(header, style=STYLES["header"])
        title_box.grid(row=0, column=0, sticky="w")
        title_box.columnconfigure(0, weight=1)

        ttk.Label(
            title_box,
            text=f"Selamat datang, {self.user.nama}",
            style=STYLES["dashboard_title"],
        ).grid(row=0, column=0, sticky="w")

        subtitle_text = f"@{self.user.username}  |  {self.user.role.title()}  |  {date.today().strftime('%d/%m/%Y')}"
        ttk.Label(title_box, text=subtitle_text, style=STYLES["dashboard_subtitle"]).grid(row=1, column=0, sticky="w", pady=(4, 0))
        ttk.Label(title_box, text=self.user.role.title(), style=STYLES["dashboard_chip"]).grid(row=2, column=0, sticky="w", pady=(12, 0))

        action_box = ttk.Frame(header, style=STYLES["header"])
        action_box.grid(row=0, column=1, sticky="e")
        ttk.Button(action_box, text="Refresh", command=self.on_refresh, style=STYLES["button_secondary"]).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(action_box, text="Logout", command=self.on_logout, style=STYLES["button_secondary"]).grid(row=0, column=1)

    def _build_content(self) -> None:
        content = ttk.Frame(self, style=STYLES["page"], padding=(24, 24))
        content.grid(row=1, column=0, sticky="nsew")
        content.columnconfigure(0, weight=0, minsize=340)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(1, weight=1)

        self._build_actions_panel(content)
        self._build_summary_panel(content)
        self._build_records_panel(content)

    def _build_actions_panel(self, parent) -> None:
        panel = ttk.Frame(parent, style=STYLES["panel_dark"], padding=(20, 20), width=340)
        panel.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=(0, 18))
        panel.columnconfigure(0, weight=1)
        panel.grid_propagate(False)

        ttk.Label(panel, text="Aksi Absensi", style=STYLES["section_title"]).grid(row=0, column=0, sticky="w")
        ttk.Label(
            panel,
            text="Pilih status, tambahkan keterangan bila perlu, lalu simpan absensi hari ini.",
            style=STYLES["panel_label"],
            wraplength=290,
            justify="left",
        ).grid(row=1, column=0, sticky="w", pady=(10, 18))

        ttk.Label(panel, text="Status", style=STYLES["panel_label"]).grid(row=2, column=0, sticky="w", pady=(0, 6))
        self.status_var = tk.StringVar(value="hadir")
        self.status_combo = ttk.Combobox(
            panel,
            textvariable=self.status_var,
            values=list(self.STATUS_OPTIONS),
            state="readonly",
            style=STYLES["form_combo"],
        )
        self.status_combo.grid(row=3, column=0, sticky="ew")

        ttk.Label(panel, text="Keterangan", style=STYLES["panel_label"]).grid(row=4, column=0, sticky="w", pady=(18, 6))
        self.keterangan_text = tk.Text(
            panel,
            height=7,
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
        self.keterangan_text.grid(row=5, column=0, sticky="ew")

        button_row = ttk.Frame(panel, style=STYLES["panel_dark"])
        button_row.grid(row=6, column=0, sticky="ew", pady=(16, 0))
        button_row.columnconfigure(0, weight=1)
        button_row.columnconfigure(1, weight=1)

        ttk.Button(button_row, text="Check In", command=self._check_in, style=STYLES["button_primary"]).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        ttk.Button(button_row, text="Check Out", command=self._check_out, style=STYLES["button_secondary"]).grid(row=0, column=1, sticky="ew", padx=(6, 0))

        action_row = ttk.Frame(panel, style=STYLES["panel_dark"])
        action_row.grid(row=7, column=0, sticky="ew", pady=(10, 0))
        action_row.columnconfigure(0, weight=1)
        action_row.columnconfigure(1, weight=1)

        ttk.Button(action_row, text="Bersihkan", command=self.clear_form, style=STYLES["button_ghost"]).grid(row=0, column=0, sticky="ew", padx=(0, 6))
        ttk.Button(action_row, text="Muat Ulang", command=self.on_refresh, style=STYLES["button_secondary"]).grid(row=0, column=1, sticky="ew", padx=(6, 0))

        self.message_var = tk.StringVar()
        self.message_label = ttk.Label(
            panel,
            textvariable=self.message_var,
            style=STYLES["panel_message"],
            wraplength=300,
            justify="left",
        )
        self.message_label.grid(row=8, column=0, sticky="w", pady=(18, 0))

    def _build_summary_panel(self, parent) -> None:
        self.summary_frame = ttk.Frame(parent, style=STYLES["page"])
        self.summary_frame.grid(row=0, column=1, sticky="ew")
        self.summary_frame.columnconfigure(0, weight=1)
        self.summary_frame.columnconfigure(1, weight=1)
        self.summary_frame.columnconfigure(2, weight=1)

        self.card_1 = self._create_card(self.summary_frame, 0)
        self.card_2 = self._create_card(self.summary_frame, 1)
        self.card_3 = self._create_card(self.summary_frame, 2)
        self._render_summary(self.summary)

    def _build_records_panel(self, parent) -> None:
        table_frame = ttk.Frame(parent, style=STYLES["surface"], padding=(16, 16))
        table_frame.grid(row=1, column=1, sticky="nsew", pady=(18, 0))
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(2, weight=1)

        ttk.Label(table_frame, text="Riwayat Absensi", style=STYLES["table_title"]).grid(row=0, column=0, sticky="w")
        self.table_hint_var = tk.StringVar()
        ttk.Label(table_frame, textvariable=self.table_hint_var, style=STYLES["helper"]).grid(row=1, column=0, sticky="w", pady=(4, 10))

        tree_container = ttk.Frame(table_frame, style=STYLES["surface"])
        tree_container.grid(row=2, column=0, sticky="nsew")
        tree_container.columnconfigure(0, weight=1)
        tree_container.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(tree_container, columns=self.COLUMNS, show="headings", height=14)
        for column in self.COLUMNS:
            self.tree.heading(column, text=self.HEADINGS[column])
            self.tree.column(column, width=self.WIDTHS[column], anchor="w")

        scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self._render_records(self.records)

    def _create_card(self, parent, index: int) -> tk.Frame:
        card = ttk.Frame(parent, style=STYLES["card"], padding=(18, 18))
        card.grid(row=0, column=index, sticky="ew", padx=(0 if index == 0 else 10, 10 if index < 2 else 0))
        card.columnconfigure(0, weight=1)
        label = ttk.Label(card, text="", style=STYLES["card_label"])
        label.grid(row=0, column=0, sticky="w")
        value = ttk.Label(card, text="", style=STYLES["card_value"])
        value.grid(row=1, column=0, sticky="w", pady=(6, 0))
        note = ttk.Label(card, text="Ringkasan hari ini", style=STYLES["card_note"])
        note.grid(row=2, column=0, sticky="w", pady=(4, 0))
        setattr(self, f"card_{index + 1}_label", label)
        setattr(self, f"card_{index + 1}_value", value)
        setattr(self, f"card_{index + 1}_note", note)
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

        if not records:
            self.table_hint_var.set("Belum ada riwayat absensi untuk ditampilkan.")
            return

        self.table_hint_var.set(f"Menampilkan {len(records)} data terbaru.")
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

    def set_message(self, text: str, color: str = COLORS["info"]) -> None:
        self.message_var.set(text)
        self.message_label.config(style=STYLES["panel_message"], foreground=color)

    def clear_form(self) -> None:
        self.status_var.set("hadir")
        self.keterangan_text.delete("1.0", "end")
        self.message_var.set("")
        self.message_label.config(style=STYLES["panel_message"], foreground=COLORS["info"])

    def _check_in(self) -> None:
        self.on_check_in(self.status_var.get(), self.keterangan_text.get("1.0", "end").strip())

    def _check_out(self) -> None:
        self.on_check_out()
