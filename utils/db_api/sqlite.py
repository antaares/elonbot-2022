import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id int primary key NOT NULL,
            Name varchar(255) NOT NULL,
            language varchar(3)
            );
"""
        self.execute(sql, commit=True)

    def create_group_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS inGroup (
            id int primary key NOT NULL,
            user varchar(50),
            count int
        );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def add_user(self, id: int, name: str, language: str = 'uz'):
        sql = """
        INSERT INTO Users(id, Name, language) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, language), commit=True)

    def calculation_group(self):
        pass

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)


    def select_user(self, id):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE id = ?"
        return self.execute(sql, (id,), fetchone=True)


    def all(self) -> list:
        sql = "SELECT id FROM Users"
        result = self.execute(sql, fetchall=True)
        return [x[0] for x in result]

    def count_users(self):
        res = self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
        if res==[]:
            return 0
        return res[0]

        
    def count_adding_users(self, id, isarray = True):
        sql = "SELECT count FROM inGroup WHERE id=?"
        res = self.execute(sql, parameters=(id,), fetchall=True)
        if res == []:
            return 0
        elif isarray:
            return res[0][0]
        return res
        
        

    def new_chat(self, id, user, count):
        res = self.count_adding_users(id, isarray=False)
        if res == [] or res == 0:
            sql = """INSERT INTO inGroup(id, user, count) VALUES(?,?,?)"""
            return self.execute(sql, parameters=(id, user, count), commit=True)
        sql = "UPDATE inGroup SET count=? WHERE id=?"
        return self.execute(sql, parameters=(count, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
