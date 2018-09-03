from dbconnect import DbConnector
from Models.Contact import Contact
import sys


class ContactController:

    TABLE_NAME = 'contacts'

    @staticmethod
    def add_contact(contact):
        if contact is None:
            return False
        global TABLE_NAME
        try:
            sql_insert = "insert into {0}(name, phone_number, created, is_deleted) values({1}, {2}, {3}, {4})"\
                .format(TABLE_NAME, contact.name, contact.phone_number, contact.created, 0)
            res = DbConnector.execute_non_query(DbConnector, sql_insert)
            return res
        except Exception as ex:
            print("Error occurred when add contact " + ex.args[0])
            return False

    @staticmethod
    def update_contact(contact):
        if contact is None:
            return False

        global TABLE_NAME
        try:
            sql_check = "select * from {0} where is_deleted = 0 and name = {1} and phone_number = {2}"\
                .format(TABLE_NAME, contact.name, contact.phone_number)
            result_exists = DbConnector.execute_fetch_all(DbConnector, sql_check)
            if result_exists is not None:
                if len(result_exists) > 0:
                    return False
                else:
                    sql_update = "update {0} set name = {1}, phone_number = {2}, created = {3} where is_deleted = 0" \
                                 " and id = {4}".format(TABLE_NAME, contact.name, contact.phone_number, contact.created, contact.contact_id)
                    result_update = DbConnector.execute_non_query(DbConnector, sql_update)
                    return result_update
        except Exception as ex:
            print("Error occured when update contact " + ex.args[0])
            return False

    @staticmethod
    def get_single(contact_id):
        if contact_id == 0:
            return None
        else:
            global TABLE_NAME
            try:
                sql_select = "select * from {0} where is_deleted = 0 and id = {1}".format(TABLE_NAME, contact_id)
                result = DbConnector.execute_fetch_one(DbConnector, sql_select)
                if result is not None:
                    contact = Contact(
                        result["id"],
                        result["name"],
                        result["phone_number"],
                        result["created"],
                        result["is_deleted"]
                    )
                    return contact
                else:
                    return None
            except Exception as ex:
                print("Error occurred while execute query: " + ex.args[0])
                return None

    @staticmethod
    def get_all():
        global TABLE_NAME
        try:
            sql_select = "select * from {0} where is_deleted = 0".format(TABLE_NAME)
            result = DbConnector.execute_fetch_all(DbConnector, sql_select)
            if result is not None and len(result) > 0:
                list_result = []
                for item in result:
                    list_result.append(
                        Contact(
                            item["id"],
                            item["name"],
                            item["phone_number"],
                            item["created"],
                            item["is_deleted"]
                        )
                    )
            else:
                return None
        except Exception as ex:
            print("Error occurred while execute query: " + ex.args[0])
            return None
