from tkinter import messagebox


class ProfileController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def load_profile(self):
        profile = self.model.load_profile()
        self.view.display_profile(profile)

    def open_edit_profile(self):
        profile = self.model.get_profile()
        self.view.open_edit_dialog(profile)

    def save_profile(self, profile_data):
        nama = profile_data.get("nama", "").strip()
        if not nama:
            messagebox.showerror("Kesalahan", "Nama tidak boleh kosong.")
            return False

        updated_profile = self.model.save_profile(profile_data)
        self.view.display_profile(updated_profile)
        messagebox.showinfo("Berhasil", "Data profil berhasil disimpan.")
        return True
