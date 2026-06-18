import customtkinter as ctk

from controller.profile_controller import ProfileController
from model.profile_model import ProfileModel
from view.main_view import ProfileView


def main() -> None:
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.minsize(980, 640)

    model = ProfileModel("data/profile_data.json")
    view = ProfileView(root)
    controller = ProfileController(model, view)
    controller.load_profile()

    root.mainloop()


if __name__ == "__main__":
    main()
