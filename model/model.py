import sqlite3
from pathlib import Path

cur_dir = Path.cwd()
db_dir = cur_dir.parent.joinpath("model", "database.db")


class Model:

    """
    This class is used for all CRUD operations on the database
    It includes only class methods, because there is no need for separate instances here
    """
    db = db_dir

    # Private method used internally in the other class methods
    @classmethod
    def _create_token_table(cls):
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS tokens (id INTEGER PRIMARY KEY,"
                                  "token TEXT)")
            conn.commit()

    @classmethod
    def insert_token(cls, token):
        cls._create_token_table()
        token = str(token)
        ## DB holds only one record for the user. So we delete it everytime a new record is put
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("DELETE FROM tokens")
            conn.commit()
        with sqlite3.connect(cls.db) as conn:
            conn.cursor().execute("INSERT INTO tokens(token) VALUES(?)", (token,))
            conn.commit()

    @classmethod
    def get_token(cls):
        with sqlite3.connect(cls.db) as conn:
            result = conn.cursor().execute("SELECT * FROM tokens")
            res = result.fetchone()
            return res

