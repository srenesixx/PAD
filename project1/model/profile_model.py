import json
from pathlib import Path
from typing import Dict, Any


class ProfileModel:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.profile: Dict[str, Any] = {}

    def get_default_profile(self) -> Dict[str, Any]:
        return {
            "nama": "Almaidah",
            "email": "almaidah3004@gmail.com",
            "alamat": "Jakarta",
            "telepon": "+62 812-3456-7890",
            "pekerjaan": "Mahasiswa / Pengembang Aplikasi",
            "tanggal_lahir": "30-04-2004",
            "deskripsi": "Saya suka belajar teknologi dan mengembangkan aplikasi yang bermanfaat.",
            "hobi": "Membaca, coding, traveling",
        }

    def load_profile(self) -> Dict[str, Any]:
        if not self.file_path.exists():
            self.profile = self.get_default_profile()
            self.save_profile(self.profile)
            return self.profile

        with self.file_path.open("r", encoding="utf-8") as file:
            self.profile = json.load(file)

        return self.profile

    def save_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        self.profile = profile
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(profile, file, indent=2, ensure_ascii=False)
        return self.profile

    def get_profile(self) -> Dict[str, Any]:
        return self.profile
