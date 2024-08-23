from src.helper import *

class DataHelper:

    def getbranch():
        con = Connection.connect_database_mssql()
        cursor = con.cursor()
        mysql = (""" SELECT * FROM `Branch` """)
        cursor.execute(mysql)
        columns = [column[0] for column in cursor.description]
        data = fix_decimal(cursor)
        result = to_json(data, columns)
        con.close()
        return result
    
    def getorder():
        con = Connection.connect_database_mysql()
        cursor = con.cursor()
        mysql = (""" SELECT * FROM `order` """)
        cursor.execute(mysql)
        columns = [column[0] for column in cursor.description]
        data = fix_decimal(cursor)
        result = to_json(data, columns)
        con.close()
        return result
    
    def addorder(data):
        con = Connection.connect_database_mysql()
        cursor = con.cursor()
        try:
            mysql = (""" INSERT INTO `order` (tracking_no, name, fat, carbs, protein) VALUES (%s, %s, %s, %s, %s) """)
            cursor.execute(mysql, (data['tracking_no'], data['name'], data['fat'], data['carbs'], data['protein']))
            con.commit()
            con.close()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            cursor.close()
            con.close()
            
    def editorder(data):
        con = Connection.connect_database_mysql()
        cursor = con.cursor()
        try:
            mysql = (""" UPDATE `order` SET name=%s, fat=%s, carbs=%s, protein=%s WHERE tracking_no=%s """)
            cursor.execute(mysql, (data['name'], data['fat'], data['carbs'], data['protein'], data['tracking_no']))
            con.commit()
            con.close()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            cursor.close()
            con.close()
            
    def deleteorder(tracking_no):
        con = Connection.connect_database_mysql()
        cursor = con.cursor()
        try:
            mysql = (""" DELETE FROM `order` WHERE tracking_no=%s """)
            cursor.execute(mysql, (tracking_no))
            con.commit()
            con.close()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            cursor.close()
            con.close()

    def test():
        print('OK')
