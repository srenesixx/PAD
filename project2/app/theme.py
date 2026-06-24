from __future__ import annotations

import tkinter as tk
from tkinter import ttk


COLORS = {
    "app_bg": "#0f172a",
    "page_bg": "#f8fafc",
    "surface_bg": "#ffffff",
    "card_bg": "#111827",
    "text": "#0f172a",
    "text_light": "#f8fafc",
    "muted": "#64748b",
    "muted_soft": "#94a3b8",
    "accent": "#2563eb",
    "accent_hover": "#1d4ed8",
    "success": "#0f766e",
    "info": "#0284c7",
    "warning": "#b45309",
    "danger": "#dc2626",
    "border": "#dbe4f0",
    "border_dark": "#334155",
    "button_bg": "#1e293b",
    "button_hover": "#334155",
    "selection_bg": "#dbeafe",
    "heading_bg": "#e2e8f0",
    "focus": "#60a5fa",
}

FONTS = {
    "base": ("Segoe UI", 10),
    "small": ("Segoe UI", 9),
    "title": ("Segoe UI", 24, "bold"),
    "title_small": ("Segoe UI", 20, "bold"),
    "section": ("Segoe UI", 15, "bold"),
    "card_value": ("Segoe UI", 19, "bold"),
    "table_heading": ("Segoe UI", 10, "bold"),
}

STYLES = {
    "root": "App.Root.TFrame",
    "page": "App.Page.TFrame",
    "login_backdrop": "App.Login.Backdrop.TFrame",
    "login_card": "App.Login.Card.TFrame",
    "login_title": "App.Login.Title.TLabel",
    "login_message": "App.Login.Message.TLabel",
    "form_label": "App.Form.Label.TLabel",
    "form_entry": "App.Form.Entry.TEntry",
    "form_combo": "App.Form.Combo.TCombobox",
    "button_primary": "App.Button.Primary.TButton",
    "button_secondary": "App.Button.Secondary.TButton",
    "button_ghost": "App.Button.Ghost.TButton",
    "header": "App.Dashboard.Header.TFrame",
    "dashboard_title": "App.Dashboard.Title.TLabel",
    "dashboard_subtitle": "App.Dashboard.Subtitle.TLabel",
    "dashboard_chip": "App.Dashboard.Chip.TLabel",
    "panel_dark": "App.Dashboard.PanelDark.TFrame",
    "surface": "App.Dashboard.Surface.TFrame",
    "section_title": "App.Dashboard.SectionTitle.TLabel",
    "meta": "App.Dashboard.Meta.TLabel",
    "panel_label": "App.Dashboard.PanelLabel.TLabel",
    "panel_message": "App.Dashboard.PanelMessage.TLabel",
    "card": "App.Dashboard.Card.TFrame",
    "card_label": "App.Dashboard.CardLabel.TLabel",
    "card_value": "App.Dashboard.CardValue.TLabel",
    "card_note": "App.Dashboard.CardNote.TLabel",
    "table_title": "App.Dashboard.TableTitle.TLabel",
    "helper": "App.Helper.TLabel",
}


def _configure_base_styles(style: ttk.Style) -> None:
    style.configure("TFrame", background=COLORS["page_bg"])
    style.configure("TLabel", background=COLORS["page_bg"], foreground=COLORS["text"])
    style.configure("TButton", font=FONTS["base"])

    style.configure(STYLES["root"], background=COLORS["app_bg"])
    style.configure(STYLES["page"], background=COLORS["page_bg"])


def _configure_login_styles(style: ttk.Style) -> None:
    style.configure(STYLES["login_backdrop"], background=COLORS["app_bg"])
    style.configure(STYLES["login_card"], background=COLORS["card_bg"], relief="flat")
    style.configure(
        STYLES["login_title"],
        background=COLORS["card_bg"],
        foreground=COLORS["text_light"],
        font=FONTS["title"],
    )
    style.configure(
        STYLES["login_message"],
        background=COLORS["card_bg"],
        foreground=COLORS["danger"],
        font=FONTS["small"],
    )
    style.configure(
        STYLES["form_label"],
        background=COLORS["card_bg"],
        foreground=COLORS["text_light"],
        font=FONTS["small"],
    )


def _configure_button_styles(style: ttk.Style) -> None:
    style.configure(
        STYLES["button_primary"],
        padding=(14, 10),
        relief="flat",
        background=COLORS["accent"],
        foreground=COLORS["text_light"],
        borderwidth=0,
        focusthickness=0,
    )
    style.map(
        STYLES["button_primary"],
        background=[("active", COLORS["accent_hover"]), ("pressed", COLORS["button_bg"]), ("disabled", COLORS["heading_bg"])],
        foreground=[("disabled", COLORS["muted_soft"])],
    )
    style.configure(
        STYLES["button_secondary"],
        padding=(14, 10),
        relief="flat",
        background=COLORS["surface_bg"],
        foreground=COLORS["text"],
        borderwidth=1,
        focusthickness=0,
    )
    style.map(
        STYLES["button_secondary"],
        background=[("active", COLORS["selection_bg"]), ("pressed", COLORS["heading_bg"])],
    )
    style.configure(
        STYLES["button_ghost"],
        padding=(10, 8),
        relief="flat",
        background=COLORS["page_bg"],
        foreground=COLORS["accent"],
        borderwidth=0,
        focusthickness=0,
    )
    style.map(
        STYLES["button_ghost"],
        background=[("active", COLORS["selection_bg"]), ("pressed", COLORS["heading_bg"])],
    )


def _configure_form_styles(style: ttk.Style) -> None:
    style.configure(
        STYLES["form_entry"],
        padding=9,
        fieldbackground="#f8fafc",
        background="#f8fafc",
        bordercolor=COLORS["accent"],
        lightcolor=COLORS["accent"],
        darkcolor=COLORS["accent"],
        relief="flat",
    )
    style.configure(
        STYLES["form_combo"],
        padding=9,
        fieldbackground="#f8fafc",
        background="#f8fafc",
        arrowcolor=COLORS["text"],
    )
    style.map(
        STYLES["form_combo"],
        fieldbackground=[("readonly", "#f8fafc")],
    )


def _configure_dashboard_styles(style: ttk.Style) -> None:
    style.configure(STYLES["header"], background=COLORS["app_bg"])
    style.configure(STYLES["dashboard_title"], background=COLORS["app_bg"], foreground=COLORS["text_light"], font=FONTS["title_small"])
    style.configure(STYLES["dashboard_subtitle"], background=COLORS["app_bg"], foreground=COLORS["muted_soft"], font=FONTS["base"])
    style.configure(
        STYLES["dashboard_chip"],
        background=COLORS["card_bg"],
        foreground=COLORS["text_light"],
        font=FONTS["small"],
    )
    style.configure(STYLES["panel_dark"], background=COLORS["card_bg"])
    style.configure(STYLES["surface"], background=COLORS["surface_bg"])
    style.configure(STYLES["section_title"], background=COLORS["card_bg"], foreground=COLORS["text_light"], font=FONTS["section"])
    style.configure(STYLES["meta"], background=COLORS["app_bg"], foreground=COLORS["muted_soft"], font=FONTS["base"])
    style.configure(STYLES["panel_label"], background=COLORS["card_bg"], foreground=COLORS["text_light"], font=FONTS["small"])
    style.configure(STYLES["panel_message"], background=COLORS["card_bg"], foreground=COLORS["info"], font=FONTS["small"])
    style.configure(STYLES["card"], background=COLORS["surface_bg"], relief="flat")
    style.configure(STYLES["card_label"], background=COLORS["surface_bg"], foreground=COLORS["muted"], font=FONTS["small"])
    style.configure(STYLES["card_value"], background=COLORS["surface_bg"], foreground=COLORS["text"], font=FONTS["card_value"])
    style.configure(STYLES["card_note"], background=COLORS["surface_bg"], foreground=COLORS["muted"], font=FONTS["small"])
    style.configure(STYLES["table_title"], background=COLORS["surface_bg"], foreground=COLORS["text"], font=("Segoe UI", 14, "bold"))
    style.configure(STYLES["helper"], background=COLORS["surface_bg"], foreground=COLORS["muted"], font=FONTS["small"])
    style.configure(
        STYLES["dashboard_chip"],
        padding=(10, 6),
        relief="flat",
    )


def _configure_data_styles(style: ttk.Style) -> None:
    style.configure(
        "Treeview",
        rowheight=34,
        background=COLORS["surface_bg"],
        fieldbackground=COLORS["surface_bg"],
        foreground=COLORS["text"],
        borderwidth=0,
        relief="flat",
    )
    style.configure(
        "Treeview.Heading",
        font=FONTS["table_heading"],
        background=COLORS["heading_bg"],
        foreground=COLORS["text"],
        relief="flat",
        padding=(8, 10),
    )
    style.map(
        "Treeview",
        background=[("selected", COLORS["selection_bg"])],
        foreground=[("selected", COLORS["text"])],
    )


def apply_theme(root: tk.Tk) -> None:
    root.configure(bg=COLORS["app_bg"])
    root.option_add("*Font", FONTS["base"])

    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    _configure_base_styles(style)
    _configure_login_styles(style)
    _configure_button_styles(style)
    _configure_form_styles(style)
    _configure_dashboard_styles(style)
    _configure_data_styles(style)
