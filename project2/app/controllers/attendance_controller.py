from __future__ import annotations

from app.models.attendance_model import AttendanceModel


class AttendanceController:
    def __init__(self) -> None:
        self.attendance_model = AttendanceModel()

    def get_dashboard_data(self, user) -> tuple[dict, list[dict]]:
        summary = self.attendance_model.get_summary(user.id, user.role)
        records = self.attendance_model.get_records(None if user.role == "dosen" else user.id)
        return summary, records

    def check_in(self, user, status: str, keterangan: str) -> tuple[bool, str]:
        return self.attendance_model.mark_check_in(user.id, status=status, keterangan=keterangan)

    def check_out(self, user) -> tuple[bool, str]:
        return self.attendance_model.mark_check_out(user.id)

