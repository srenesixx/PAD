import customtkinter as ctk


class EditProfileView:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.colors = {
            "bg": "#f4efe7",
            "surface": "#fffdfa",
            "surface_alt": "#f8f3ec",
            "text": "#1f2937",
            "muted": "#6b7280",
            "accent": "#b58a3c",
            "accent_hover": "#9b742c",
            "border": "#e7ddd0",
        }

    def show(self, profile):
        self.window = ctk.CTkToplevel(self.parent)
        self.window.title("Edit Profil")
        self.window.geometry("760x760")
        self.window.minsize(660, 640)
        self.window.configure(fg_color=self.colors["bg"])
        self.window.transient(self.parent)
        self.window.grab_set()

        self._build_ui(profile)
        self._center_window()

    def _center_window(self):
        self.window.update_idletasks()
        parent_x = self.parent.winfo_rootx()
        parent_y = self.parent.winfo_rooty()
        parent_w = self.parent.winfo_width()
        parent_h = self.parent.winfo_height()
        width = self.window.winfo_reqwidth()
        height = self.window.winfo_reqheight()
        x = parent_x + max((parent_w - width) // 2, 20)
        y = parent_y + max((parent_h - height) // 2, 20)
        self.window.geometry(f"+{x}+{y}")

    def _build_ui(self, profile):
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(
            self.window,
            fg_color="#1f2937",
            corner_radius=24,
        )
        header.grid(row=0, column=0, sticky="ew", padx=18, pady=(18, 12))
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header,
            text="Edit Profil",
            text_color="#d7b56d",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=22, pady=(18, 2))

        ctk.CTkLabel(
            header,
            text="Perbarui data pribadi dengan tampilan form yang rapi dan mudah diisi.",
            text_color="#f8fafc",
            font=ctk.CTkFont(size=22, weight="bold"),
            wraplength=660,
            justify="left",
        ).grid(row=1, column=0, sticky="w", padx=22)

        ctk.CTkLabel(
            header,
            text="Setiap perubahan akan langsung tersimpan ke file profil.",
            text_color="#cbd5e1",
            font=ctk.CTkFont(size=12),
        ).grid(row=2, column=0, sticky="w", padx=22, pady=(4, 18))

        body = ctk.CTkScrollableFrame(
            self.window,
            fg_color=self.colors["surface"],
            corner_radius=24,
            border_width=1,
            border_color=self.colors["border"],
        )
        body.grid(row=1, column=0, sticky="nsew", padx=18, pady=(0, 18))
        body.grid_columnconfigure(0, weight=1)
        body.grid_columnconfigure(1, weight=1)

        self.entries = {}
        field_specs = [
            ("nama", "Nama Lengkap", profile.get("nama", ""), 0, 0, False),
            ("pekerjaan", "Pekerjaan", profile.get("pekerjaan", ""), 0, 1, False),
            ("email", "Email", profile.get("email", ""), 1, 0, False),
            ("telepon", "Telepon", profile.get("telepon", ""), 1, 1, False),
            ("alamat", "Alamat", profile.get("alamat", ""), 2, 0, False),
            ("tanggal_lahir", "Tanggal Lahir", profile.get("tanggal_lahir", ""), 2, 1, False),
            ("hobi", "Hobi", profile.get("hobi", ""), 3, 0, False),
        ]

        for key, label_text, default_value, row, col, multiline in field_specs:
            self._field_card(body, key, label_text, default_value, row, col, multiline)

        desc_card = ctk.CTkFrame(
            body,
            fg_color=self.colors["surface_alt"],
            corner_radius=18,
        )
        desc_card.grid(row=4, column=0, columnspan=2, sticky="ew", padx=8, pady=10)
        desc_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            desc_card,
            text="Deskripsi",
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=12, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 6))

        desc_box = ctk.CTkTextbox(
            desc_card,
            height=130,
            corner_radius=14,
            fg_color="#ffffff",
            border_color=self.colors["border"],
            border_width=1,
            text_color=self.colors["text"],
            scrollbar_button_color=self.colors["accent"],
            scrollbar_button_hover_color=self.colors["accent_hover"],
        )
        desc_box.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 16))
        desc_box.insert("1.0", profile.get("deskripsi", ""))
        self.entries["deskripsi"] = desc_box

        actions = ctk.CTkFrame(
            self.window,
            fg_color="transparent",
            corner_radius=0,
        )
        actions.grid(row=2, column=0, sticky="ew", padx=18, pady=(0, 18))
        actions.grid_columnconfigure(0, weight=1)
        actions.grid_columnconfigure(1, weight=0)

        ctk.CTkButton(
            actions,
            text="Batal",
            fg_color="#e5e7eb",
            hover_color="#d1d5db",
            text_color=self.colors["text"],
            corner_radius=16,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.window.destroy,
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkButton(
            actions,
            text="Simpan Perubahan",
            fg_color=self.colors["accent"],
            hover_color=self.colors["accent_hover"],
            text_color="#ffffff",
            corner_radius=16,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._save,
        ).grid(row=0, column=1, sticky="e")

        self.window.bind("<Return>", lambda event: self._save())
        self.window.bind("<Escape>", lambda event: self.window.destroy())

    def _field_card(self, parent, key, label_text, default_value, row, col, multiline):
        card = ctk.CTkFrame(
            parent,
            fg_color=self.colors["surface_alt"],
            corner_radius=18,
        )
        card.grid(row=row, column=col, sticky="ew", padx=8, pady=10)
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            card,
            text=label_text,
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=12, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 6))

        if multiline:
            widget = ctk.CTkTextbox(
                card,
                height=90,
                corner_radius=14,
                fg_color="#ffffff",
                border_color=self.colors["border"],
                border_width=1,
                text_color=self.colors["text"],
            )
            widget.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 16))
            widget.insert("1.0", default_value)
        else:
            widget = ctk.CTkEntry(
                card,
                height=40,
                corner_radius=14,
                fg_color="#ffffff",
                border_color=self.colors["border"],
                text_color=self.colors["text"],
                placeholder_text=label_text,
            )
            widget.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 16))
            widget.insert(0, default_value)

        self.entries[key] = widget

    def _save(self):
        data = {}
        for key, widget in self.entries.items():
            if isinstance(widget, ctk.CTkTextbox):
                data[key] = widget.get("1.0", "end").strip()
            else:
                data[key] = widget.get().strip()

        if self.controller.save_profile(data):
            self.window.destroy()
