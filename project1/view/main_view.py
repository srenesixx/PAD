import customtkinter as ctk

from view.edit_profile_view import EditProfileView


class ProfileView:
    def __init__(self, root):
        self.root = root
        self.controller = None

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.colors = {
            "bg": "#f4efe7",
            "surface": "#fffdfa",
            "surface_alt": "#f8f3ec",
            "text": "#1f2937",
            "muted": "#6b7280",
            "accent": "#b58a3c",
            "accent_hover": "#9b742c",
            "border": "#e7ddd0",
            "chip_bg": "#efe4d2",
            "chip_text": "#7a5a24",
            "hero_bg": "#1f2937",
            "hero_text": "#f9fafb",
        }

        self.root.title("Profil Pengguna")
        self.root.configure(fg_color=self.colors["bg"])
        self.root.geometry("1180x720")
        self.root.minsize(980, 640)

        self._build_ui()
        self.root.bind("<Configure>", self._on_root_configure)
        self.root.after(50, self._update_wrap_lengths)

    def set_controller(self, controller):
        self.controller = controller

    def _build_ui(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.shell = ctk.CTkFrame(
            self.root,
            fg_color=self.colors["bg"],
            corner_radius=0,
        )
        self.shell.grid(row=0, column=0, sticky="nsew")
        self.shell.grid_columnconfigure(0, weight=1)
        self.shell.grid_rowconfigure(1, weight=1)

        self._build_content()

    def _build_content(self):
        content = ctk.CTkFrame(
            self.shell,
            fg_color="transparent",
            corner_radius=0,
        )
        content.grid(row=1, column=0, sticky="nsew", padx=28, pady=(6, 28))
        content.grid_columnconfigure(0, weight=0)
        content.grid_columnconfigure(1, weight=1)
        content.grid_rowconfigure(0, weight=1)

        self.left_panel = ctk.CTkFrame(
            content,
            fg_color=self.colors["surface"],
            corner_radius=28,
            border_width=1,
            border_color=self.colors["border"],
            width=290,
        )
        self.left_panel.grid(row=0, column=0, sticky="nsw", padx=(0, 18))
        self.left_panel.grid_columnconfigure(0, weight=1)

        self.right_panel = ctk.CTkScrollableFrame(
            content,
            fg_color=self.colors["surface"],
            corner_radius=28,
            border_width=1,
            border_color=self.colors["border"],
        )
        self.right_panel.grid(row=0, column=1, sticky="nsew")
        self.right_panel.grid_columnconfigure(0, weight=1)

        self._build_profile_card()
        self._build_detail_sections()

    def _build_profile_card(self):
        hero = ctk.CTkFrame(
            self.left_panel,
            fg_color=self.colors["hero_bg"],
            corner_radius=24,
        )
        hero.grid(row=0, column=0, padx=18, pady=18, sticky="ew")
        hero.grid_columnconfigure(0, weight=1)

        self.avatar = ctk.CTkLabel(
            hero,
            text="A",
            width=92,
            height=92,
            corner_radius=46,
            fg_color="#d7b56d",
            text_color="#1f2937",
            font=ctk.CTkFont(size=34, weight="bold"),
        )
        self.avatar.grid(row=0, column=0, pady=(24, 14))

        self.name_label = ctk.CTkLabel(
            hero,
            text="Nama",
            text_color=self.colors["hero_text"],
            font=ctk.CTkFont(size=24, weight="bold"),
            wraplength=220,
            justify="center",
        )
        self.name_label.grid(row=1, column=0, padx=20)

        self.job_label = ctk.CTkLabel(
            hero,
            text="Pekerjaan",
            text_color="#cbd5e1",
            font=ctk.CTkFont(size=13),
            wraplength=220,
            justify="center",
        )
        self.job_label.grid(row=2, column=0, padx=20, pady=(6, 20))

        action_bar = ctk.CTkFrame(
            self.left_panel,
            fg_color="transparent",
            corner_radius=0,
        )
        action_bar.grid(row=1, column=0, padx=18, sticky="ew")
        action_bar.grid_columnconfigure(0, weight=1)

        self.edit_button = ctk.CTkButton(
            action_bar,
            text="Edit Profil",
            corner_radius=18,
            fg_color=self.colors["accent"],
            hover_color=self.colors["accent_hover"],
            text_color="#ffffff",
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self._on_edit_clicked,
        )
        self.edit_button.grid(row=0, column=0, sticky="ew")

        self.subtitle = ctk.CTkLabel(
            self.left_panel,
            text="Perubahan tersimpan otomatis ke data profil.",
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=12),
            wraplength=220,
            justify="center",
        )
        self.subtitle.grid(row=2, column=0, padx=22, pady=(14, 22))

        self._build_mini_cards()

    def _build_mini_cards(self):
        mini_wrap = ctk.CTkFrame(
            self.left_panel,
            fg_color="transparent",
            corner_radius=0,
        )
        mini_wrap.grid(row=3, column=0, padx=18, pady=(0, 18), sticky="ew")
        mini_wrap.grid_columnconfigure(0, weight=1)

        self.mini_email = self._info_mini_card(mini_wrap, "Email", "email_value", 0)
        self.mini_phone = self._info_mini_card(mini_wrap, "Telepon", "telepon_value", 1)

    def _info_mini_card(self, parent, title, key, row):
        card = ctk.CTkFrame(
            parent,
            fg_color=self.colors["surface_alt"],
            corner_radius=18,
        )
        card.grid(row=row, column=0, sticky="ew", pady=6)
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            card,
            text=title,
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=11, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=14, pady=(12, 2))

        label = ctk.CTkLabel(
            card,
            text="",
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=12),
            wraplength=220,
            justify="left",
        )
        label.grid(row=1, column=0, sticky="w", padx=14, pady=(0, 12))
        setattr(self, key, label)
        return card

    def _build_detail_sections(self):
        self._section_title(self.right_panel, "Detail Profil", "Semua informasi utama dalam satu tampilan yang bersih dan terstruktur.").grid(
            row=0, column=0, sticky="ew", padx=6, pady=(4, 12)
        )

        info_grid = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        info_grid.grid(row=1, column=0, sticky="ew", padx=6)
        info_grid.grid_columnconfigure(0, weight=1)
        info_grid.grid_columnconfigure(1, weight=1)

        rows = [
            ("Email", "email_value", 0, 0),
            ("Alamat", "alamat_value", 0, 1),
            ("Telepon", "telepon_value", 1, 0),
            ("Tanggal Lahir", "tanggal_value", 1, 1),
        ]

        self.labels = {}
        for title, key, r, c in rows:
            card = self._detail_card(info_grid, title, key)
            card.grid(row=r, column=c, sticky="ew", padx=8, pady=8)
            self.labels[key] = getattr(self, key)

        about_title = self._section_title(
            self.right_panel,
            "Tentang Saya",
            "Ringkasan singkat yang terasa personal dan tetap mudah dipindai.",
        )
        about_title.grid(row=2, column=0, sticky="ew", padx=6, pady=(18, 12))

        self.description = ctk.CTkLabel(
            self.right_panel,
            text="Deskripsi",
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=14),
            wraplength=620,
            justify="left",
        )
        self.description.grid(row=3, column=0, sticky="ew", padx=10)

        self.hobbies_frame = ctk.CTkFrame(
            self.right_panel,
            fg_color=self.colors["surface_alt"],
            corner_radius=22,
        )
        self.hobbies_frame.grid(row=4, column=0, sticky="ew", padx=6, pady=(18, 10))
        self.hobbies_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.hobbies_frame,
            text="Hobi",
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=12, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=18, pady=(16, 8))

        self.hobby_label = ctk.CTkLabel(
            self.hobbies_frame,
            text="",
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=13),
            wraplength=620,
            justify="left",
        )
        self.hobby_label.grid(row=1, column=0, sticky="ew", padx=18, pady=(0, 18))

    def _section_title(self, parent, title, subtitle):
        wrap = ctk.CTkFrame(parent, fg_color="transparent")
        wrap.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(
            wrap,
            text=title,
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=18, weight="bold"),
        ).grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(
            wrap,
            text=subtitle,
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=12),
            wraplength=640,
            justify="left",
        ).grid(row=1, column=0, sticky="w", pady=(4, 0))
        return wrap

    def _detail_card(self, parent, title, key):
        card = ctk.CTkFrame(
            parent,
            fg_color=self.colors["surface_alt"],
            corner_radius=20,
        )
        card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            card,
            text=title,
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=11, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=16, pady=(14, 2))

        label = ctk.CTkLabel(
            card,
            text="",
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=13),
            wraplength=320,
            justify="left",
        )
        label.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 14))
        setattr(self, key, label)
        return card

    def _stat_chip(self, parent, title, value):
        chip = ctk.CTkFrame(
            parent,
            fg_color=self.colors["surface_alt"],
            corner_radius=16,
        )
        chip.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(
            chip,
            text=title,
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=11, weight="bold"),
        ).grid(row=0, column=0, sticky="w", padx=12, pady=(10, 0))
        ctk.CTkLabel(
            chip,
            text=value,
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=13, weight="bold"),
        ).grid(row=1, column=0, sticky="w", padx=12, pady=(2, 10))
        return chip

    def display_profile(self, profile):
        name = profile.get("nama", "")
        self.name_label.configure(text=name or "Nama")
        self.job_label.configure(text=profile.get("pekerjaan", "") or "Pekerjaan")
        self.email_value.configure(text=profile.get("email", "") or "-")
        self.alamat_value.configure(text=profile.get("alamat", "") or "-")
        self.telepon_value.configure(text=profile.get("telepon", "") or "-")
        self.tanggal_value.configure(text=profile.get("tanggal_lahir", "") or "-")
        self.description.configure(text=profile.get("deskripsi", "") or "Tidak ada deskripsi.")
        self.hobby_label.configure(text=profile.get("hobi", "") or "-")
        self.avatar.configure(text=(name[:1].upper() if name else "P"))
        self._update_wrap_lengths()

    def _on_root_configure(self, event):
        self._update_wrap_lengths()

    def _update_wrap_lengths(self):
        if not hasattr(self, "right_panel"):
            return

        right_width = max(self.right_panel.winfo_width() - 60, 520)
        self.description.configure(wraplength=right_width)
        self.hobby_label.configure(wraplength=right_width)
        for label in self.labels.values():
            label.configure(wraplength=max((right_width - 120) / 2, 220))

        self.name_label.configure(wraplength=max(self.left_panel.winfo_width() - 60, 200))
        self.job_label.configure(wraplength=max(self.left_panel.winfo_width() - 60, 200))
        self.subtitle.configure(wraplength=max(self.left_panel.winfo_width() - 60, 200))

    def _on_edit_clicked(self):
        if self.controller:
            self.controller.open_edit_profile()

    def open_edit_dialog(self, profile):
        EditProfileView(self.root, self.controller).show(profile)
