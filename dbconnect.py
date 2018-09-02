import sqlite3
from Config import app_config as appconfig


class DbConnector:

    conn = None
    dbFile = appconfig.Configuration.default()["datasource"]
    cursor = None

    @staticmethod
    def __open_connect():
        try:
            global conn, dbFile, cursor
            conn = sqlite3.connect(dbFile)
            cursor = conn.cursor()
        except sqlite3.Error as e:
            print("Error when connect to database: " + e.args[0])

    def execute_fetch(self, sql):
        self.__open_connect()
        global cursor
        cursor.execute(sql)

    def execute_non_query(self, sql):
        self.__open_connect()
