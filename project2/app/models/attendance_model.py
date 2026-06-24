from __future__ import annotations

from datetime import date, datetime
from typing import Any, Dict, List, Optional

from app.database import get_connection


class AttendanceModel:
    """Business logic for attendance records."""

    def _today(self) -> str:
        return date.today().isoformat()

    def _now_time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    def get_today_record(self, user_id: int) -> Optional[Dict[str, Any]]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM absensi
            WHERE user_id = ? AND tanggal = ?
            LIMIT 1
            """,
            (user_id, self._today()),
        )
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def mark_check_in(self, user_id: int, status: str = "hadir", keterangan: str = "") -> tuple[bool, str]:
        now = self._now_time()
        today = self._today()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, jam_masuk, jam_pulang
            FROM absensi
            WHERE user_id = ? AND tanggal = ?
            LIMIT 1
            """,
            (user_id, today),
        )
        row = cursor.fetchone()

        if row and row["jam_masuk"]:
            conn.close()
            return False, "Absensi masuk untuk hari ini sudah tercatat."

        if row:
            cursor.execute(
                """
                UPDATE absensi
                SET jam_masuk = ?, status = ?, keterangan = ?
                WHERE id = ?
                """,
                (now, status, keterangan.strip(), row["id"]),
            )
        else:
            cursor.execute(
                """
                INSERT INTO absensi (user_id, tanggal, jam_masuk, status, keterangan)
                VALUES (?, ?, ?, ?, ?)
                """,
                (user_id, today, now, status, keterangan.strip()),
            )

        conn.commit()
        conn.close()
        return True, f"Absensi masuk berhasil pada {now}."

    def mark_check_out(self, user_id: int) -> tuple[bool, str]:
        now = self._now_time()
        today = self._today()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, jam_masuk, jam_pulang
            FROM absensi
            WHERE user_id = ? AND tanggal = ?
            LIMIT 1
            """,
            (user_id, today),
        )
        row = cursor.fetchone()

        if row is None or not row["jam_masuk"]:
            conn.close()
            return False, "Absensi masuk hari ini belum dilakukan."

        if row["jam_pulang"]:
            conn.close()
            return False, "Absensi pulang untuk hari ini sudah tercatat."

        cursor.execute(
            """
            UPDATE absensi
            SET jam_pulang = ?
            WHERE id = ?
            """,
            (now, row["id"]),
        )
        conn.commit()
        conn.close()
        return True, f"Absensi pulang berhasil pada {now}."

    def get_records(self, user_id: Optional[int] = None, limit: int = 100) -> List[Dict[str, Any]]:
        conn = get_connection()
        cursor = conn.cursor()

        params: list[Any] = []
        user_clause = ""
        if user_id is not None:
            user_clause = "WHERE a.user_id = ?"
            params.append(user_id)

        params.append(limit)
        cursor.execute(
            f"""
            SELECT
                a.id,
                a.user_id,
                u.username,
                u.nama,
                u.role,
                a.tanggal,
                a.jam_masuk,
                a.jam_pulang,
                a.status,
                a.keterangan,
                a.created_at
            FROM absensi a
            JOIN users u ON u.id = a.user_id
            {user_clause}
            ORDER BY a.tanggal DESC, a.created_at DESC
            LIMIT ?
            """,
            params,
        )
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_summary(self, user_id: int, role: str) -> Dict[str, Any]:
        conn = get_connection()
        cursor = conn.cursor()
        today = self._today()

        if role == "dosen":
            cursor.execute("SELECT COUNT(*) AS total FROM users")
            total_users = cursor.fetchone()["total"]
            cursor.execute(
                """
                SELECT COUNT(*) AS total
                FROM absensi
                WHERE tanggal = ? AND jam_masuk IS NOT NULL
                """,
                (today,),
            )
            present_today = cursor.fetchone()["total"]
            cursor.execute(
                """
                SELECT COUNT(*) AS total
                FROM absensi
                WHERE tanggal = ? AND jam_masuk IS NOT NULL AND jam_pulang IS NOT NULL
                """,
                (today,),
            )
            finished_today = cursor.fetchone()["total"]
            conn.close()
            return {
                "label_1": "Total User",
                "value_1": total_users,
                "label_2": "Sudah Masuk Hari Ini",
                "value_2": present_today,
                "label_3": "Sudah Pulang Hari Ini",
                "value_3": finished_today,
            }

        cursor.execute(
            """
            SELECT jam_masuk, jam_pulang, status, keterangan, tanggal
            FROM absensi
            WHERE user_id = ? AND tanggal = ?
            LIMIT 1
            """,
            (user_id, today),
        )
        row = cursor.fetchone()
        conn.close()

        if row is None:
            return {
                "label_1": "Status Hari Ini",
                "value_1": "Belum absen",
                "label_2": "Masuk",
                "value_2": "-",
                "label_3": "Pulang",
                "value_3": "-",
            }

        return {
            "label_1": "Status Hari Ini",
            "value_1": row["status"] or "hadir",
            "label_2": "Masuk",
            "value_2": row["jam_masuk"] or "-",
            "label_3": "Pulang",
            "value_3": row["jam_pulang"] or "-",
        }

