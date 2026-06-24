from __future__ import annotations

import tkinter as tk
from tkinter import ttk


COLORS = {
    "app_bg": "#0b1220",
    "page_bg": "#f5f7fb",
    "card_bg": "#111827",
    "surface_bg": "#ffffff",
    "text": "#0f172a",
    "text_light": "#e2e8f0",
    "muted": "#94a3b8",
    "muted_dark": "#64748b",
    "accent": "#38bdf8",
    "accent_hover": "#0ea5e9",
    "danger": "#f87171",
    "border": "#e2e8f0",
    "border_dark": "#334155",
    "button_bg": "#1f2937",
    "button_hover": "#334155",
    "selection_bg": "#dbeafe",
    "heading_bg": "#e2e8f0",
}

FONTS = {
    "base": ("Segoe UI", 10),
    "label": ("Segoe UI", 9),
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
    "login_subtitle": "App.Login.Subtitle.TLabel",
    "login_hint": "App.Login.Hint.TLabel",
    "login_message": "App.Login.Message.TLabel",
    "form_label": "App.Form.Label.TLabel",
    "form_entry": "App.Form.Entry.TEntry",
    "form_combo": "App.Form.Combo.TCombobox",
    "button_primary": "App.Button.Primary.TButton",
    "button_secondary": "App.Button.Secondary.TButton",
    "header": "App.Dashboard.Header.TFrame",
    "dashboard_title": "App.Dashboard.Title.TLabel",
    "panel_dark": "App.Dashboard.PanelDark.TFrame",
    "surface": "App.Dashboard.Surface.TFrame",
    "section_title": "App.Dashboard.SectionTitle.TLabel",
    "meta": "App.Dashboard.Meta.TLabel",
    "panel_label": "App.Dashboard.PanelLabel.TLabel",
    "panel_message": "App.Dashboard.PanelMessage.TLabel",
    "card": "App.Dashboard.Card.TFrame",
    "card_label": "App.Dashboard.CardLabel.TLabel",
    "card_value": "App.Dashboard.CardValue.TLabel",
    "table_title": "App.Dashboard.TableTitle.TLabel",
}


def apply_theme(root: tk.Tk) -> None:
    root.configure(bg=COLORS["app_bg"])
    root.option_add("*Font", FONTS["base"])

    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    style.configure(STYLES["root"], background=COLORS["app_bg"])
    style.configure(STYLES["page"], background=COLORS["page_bg"])
    style.configure(STYLES["login_backdrop"], background=COLORS["app_bg"])
    style.configure(STYLES["login_card"], background=COLORS["card_bg"], relief="flat")
    style.configure(STYLES["login_title"], background=COLORS["card_bg"], foreground="#f8fafc", font=FONTS["title"])
    style.configure(STYLES["login_subtitle"], background=COLORS["card_bg"], foreground=COLORS["muted"], font=FONTS["base"])
    style.configure(STYLES["login_hint"], background=COLORS["card_bg"], foreground=COLORS["muted_dark"], font=FONTS["label"])
    style.configure(STYLES["login_message"], background=COLORS["card_bg"], foreground=COLORS["danger"], font=FONTS["label"])
    style.configure(STYLES["form_label"], background=COLORS["card_bg"], foreground=COLORS["text_light"], font=FONTS["label"])
    style.configure("TLabel", background=COLORS["page_bg"], foreground=COLORS["text"])
    style.configure(
        STYLES["button_primary"],
        padding=(14, 10),
        relief="flat",
        background=COLORS["button_bg"],
        foreground="#f8fafc",
        borderwidth=0,
        focusthickness=0,
    )
    style.map(
        STYLES["button_primary"],
        background=[("active", COLORS["button_hover"]), ("pressed", COLORS["app_bg"])],
        foreground=[("disabled", COLORS["muted"])],
    )
    style.configure(
        STYLES["button_secondary"],
        padding=(14, 10),
        relief="flat",
        background=COLORS["surface_bg"],
        foreground=COLORS["text"],
        borderwidth=0,
        focusthickness=0,
    )
    style.map(
        STYLES["button_secondary"],
        background=[("active", COLORS["selection_bg"]), ("pressed", COLORS["heading_bg"])],
    )
    style.configure(
        STYLES["form_entry"],
        padding=8,
        fieldbackground="#ffffff",
        background="#ffffff",
        bordercolor="#cbd5e1",
        lightcolor="#cbd5e1",
        darkcolor="#cbd5e1",
        relief="flat",
    )
    style.configure(
        STYLES["form_combo"],
        padding=8,
        fieldbackground="#ffffff",
        background="#ffffff",
        arrowcolor=COLORS["text"],
    )
    style.map(STYLES["form_combo"], fieldbackground=[("readonly", "#ffffff")])
    style.configure(STYLES["header"], background=COLORS["app_bg"])
    style.configure(STYLES["panel_dark"], background=COLORS["card_bg"])
    style.configure(STYLES["surface"], background=COLORS["surface_bg"])
    style.configure(STYLES["section_title"], background=COLORS["card_bg"], foreground="#f8fafc", font=FONTS["section"])
    style.configure(STYLES["dashboard_title"], background=COLORS["app_bg"], foreground="#f8fafc", font=FONTS["title_small"])
    style.configure(STYLES["meta"], background=COLORS["app_bg"], foreground=COLORS["muted"], font=FONTS["base"])
    style.configure(STYLES["panel_label"], background=COLORS["card_bg"], foreground="#f8fafc", font=FONTS["label"])
    style.configure(STYLES["panel_message"], background=COLORS["card_bg"], foreground=COLORS["accent"], font=FONTS["label"])
    style.configure(STYLES["card"], background=COLORS["surface_bg"], relief="flat")
    style.configure(STYLES["card_label"], background=COLORS["surface_bg"], foreground=COLORS["muted_dark"], font=FONTS["label"])
    style.configure(STYLES["card_value"], background=COLORS["surface_bg"], foreground=COLORS["text"], font=FONTS["card_value"])
    style.configure(STYLES["table_title"], background=COLORS["surface_bg"], foreground=COLORS["text"], font=("Segoe UI", 14, "bold"))
    style.configure(
        "Treeview",
        rowheight=32,
        background="#ffffff",
        fieldbackground="#ffffff",
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
