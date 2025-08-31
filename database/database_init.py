import sqlite3
from pathlib import Path

DB_PATH = Path("database.sqlite")
SCHEMA_PATH = Path(__file__).with_name("schema.sql")
SEED_PATH = Path(__file__).with_name("seed.sql")

def connect():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def main():
    try:
        # Connect to SQLite Database and create a cursor
        connection = connect()
        cursor = connection.cursor()
        print('DB Init')

        # Execute the schema and seed scripts
        cursor.executescript(read_file(SCHEMA_PATH))
        cursor.executescript(read_file(SEED_PATH))

        # Close the cursor after use
        cursor.close()

    except sqlite3.Error as error:
        print('Error occurred -', error)

    finally:
        if connection:
            connection.close()
            print('SQLite Connection closed')

if __name__ == "__main__":
    main()
