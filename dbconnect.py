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
            cursor.fetchall()
        except sqlite3.Error as e:
            print("Error when connect to database: " + e.args[0])

    @staticmethod
    def execute_fetch(self, sql):
        try:
            self.__open_connect()
            global cursor
            cursor.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error when execute fetch data " + e.args[0])

    @staticmethod
    def execute_non_query(self, sql):
        try:
            self.__open_connect()
            global cursor, conn
            cursor.execute(sql)
            conn.commit()
        except sqlite3.Error as e:
            print("Error when execute non-query " + e.args[0])
