from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from app.controllers.attendance_controller import AttendanceController
from app.controllers.auth_controller import AuthController
from app.views.dashboard_view import DashboardView
from app.views.login_view import LoginView
from app.theme import apply_theme


class AppController:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.auth_controller = AuthController()
        self.attendance_controller = AttendanceController()
        self.current_user = None
        self.current_view = None
        self._configure_root()
        self.show_login()

    def _configure_root(self) -> None:
        self.root.title("Sistem Absensi Terpadu")
        self.root.geometry("1320x800")
        self.root.minsize(1180, 720)
        apply_theme(self.root)

    def clear_current_view(self) -> None:
        if self.current_view is not None:
            self.current_view.destroy()
            self.current_view = None

    def show_login(self) -> None:
        self.clear_current_view()
        self.current_view = LoginView(self.root, self.handle_login)
        self.current_view.pack(fill="both", expand=True)

    def handle_login(self, username: str, password: str) -> None:
        user = self.auth_controller.login(username, password)
        if user is None:
            self.current_view.show_error("Username atau password salah.")
            return

        self.current_user = user
        self.show_dashboard()

    def show_dashboard(self) -> None:
        self.clear_current_view()
        summary, records = self.attendance_controller.get_dashboard_data(self.current_user)
        self.current_view = DashboardView(
            self.root,
            self.current_user,
            summary,
            records,
            self.handle_check_in,
            self.handle_check_out,
            self.refresh_dashboard,
            self.logout,
        )
        self.current_view.pack(fill="both", expand=True)

    def refresh_dashboard(self) -> None:
        if self.current_user is None:
            return
        summary, records = self.attendance_controller.get_dashboard_data(self.current_user)
        self.current_view.update_data(summary, records)
        self.current_view.set_message("Data berhasil diperbarui.")

    def handle_check_in(self, status: str, keterangan: str) -> None:
        success, message = self.attendance_controller.check_in(self.current_user, status, keterangan)
        if success:
            self.refresh_dashboard()
            self.current_view.clear_form()
            self.current_view.set_message(message)
            messagebox.showinfo("Berhasil", message)
        else:
            self.current_view.set_message(message, color="#f87171")
            messagebox.showwarning("Gagal", message)

    def handle_check_out(self) -> None:
        success, message = self.attendance_controller.check_out(self.current_user)
        if success:
            self.refresh_dashboard()
            self.current_view.clear_form()
            self.current_view.set_message(message)
            messagebox.showinfo("Berhasil", message)
        else:
            self.current_view.set_message(message, color="#f87171")
            messagebox.showwarning("Gagal", message)

    def logout(self) -> None:
        self.current_user = None
        self.show_login()
