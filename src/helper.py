from decimal import *
from .config import mysql_hostIP, mysql_dataBase, mysql_userName, mysql_passWord, mssql_hostIP, mssql_dataBase, mssql_userName, mssql_passWord
import pymssql, pymysql
from datetime import *
from pytz import timezone

class Connection:

    def connect_database_mssql():
        host = mssql_hostIP
        user = mssql_userName
        password = mssql_passWord
        db = mssql_dataBase
        return pymssql.connect(host, user, password, db)
    
    def connect_database_mysql():
        host = mysql_hostIP
        user = mysql_userName
        password = mysql_passWord
        db = mysql_dataBase
        return pymysql.connect(host=host, user=user, password=password, db=db)

class GeneralHelper:

    def get_current_datetime():
        utc_time = datetime.now(timezone('UTC'))
        my_zone = 'Asia/Bangkok'
        now_date = utc_time.astimezone(timezone(my_zone))
        return now_date

def to_json(data, columns):
    results = []
    for row in data:
        results.append(dict(zip(columns, row)))
    return results

def fix_decimal(cursor):
    data = cursor.fetchall()
    ret = []
    for row in range(len(data)):
        ret.append(list(data[row]))
        for col in range(len(ret[row])):
            if type(ret[row][col]) == type(Decimal(1.0)):
                ret[-1][col] = str(ret[row][col])
    return ret
