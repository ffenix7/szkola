"""Small helper to repair local SQLite DBs used by the app.

Usage:
    python scripts/upgrade_db.py

This script will:
 - Ensure `data/users.db` exists and add a `ranking` INTEGER column to `users` table if it is missing.
 - Create an empty `data/tournaments.db` file if it doesn't exist (tables are created by the app).
"""
from pathlib import Path
import sqlite3
import sys


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data'
DATA_DIR.mkdir(exist_ok=True)


def ensure_users_ranking(db_path: Path):
    if not db_path.exists():
        print(f"Creating new database: {db_path}")
        conn = sqlite3.connect(db_path)
        conn.close()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    try:
        cur.execute("PRAGMA table_info(users)")
        rows = cur.fetchall()
    except sqlite3.DatabaseError as e:
        print(f"Database error checking users table: {e}")
        conn.close()
        return

    cols = [r[1] for r in rows]
    if 'ranking' in cols:
        print("Column 'ranking' already exists in users table.")
    else:
        try:
            cur.execute("ALTER TABLE users ADD COLUMN ranking INTEGER DEFAULT 0")
            conn.commit()
            print("Added 'ranking' column to users table.")
        except sqlite3.OperationalError as e:
            # If table doesn't exist, or ALTER not possible, notify user.
            print(f"Could not add column: {e}")
            print("If the 'users' table does not exist yet, start the app once or recreate the DB.")
    conn.close()


def ensure_tournaments_db(db_path: Path):
    if not db_path.exists():
        print(f"Creating empty tournaments DB at: {db_path}")
        conn = sqlite3.connect(db_path)
        conn.close()
    else:
        print(f"Tournaments DB already exists: {db_path}")


def main():
    users_db = DATA_DIR / 'users.db'
    tournaments_db = DATA_DIR / 'tournaments.db'

    ensure_users_ranking(users_db)
    ensure_tournaments_db(tournaments_db)

    print("Done. If you still see schema errors, consider removing 'data/users.db' to recreate it from models (data will be lost).")


if __name__ == '__main__':
    main()
