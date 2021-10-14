import cx_Oracle
import json
from dtos import mensaje


def output_type_handler(cursor, name, default_type, size, precision, scale):
    if default_type == cx_Oracle.DB_TYPE_CLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG, arraysize=cursor.arraysize)
    if default_type == cx_Oracle.DB_TYPE_BLOB:
        return cursor.var(cx_Oracle.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)


def main():

    connection = cx_Oracle.connect(user="", password="",
                                   dsn="rds.test.integrator.co.ua.la:1521/PTSDB")
    connection.outputtypehandler = output_type_handler
    cursor = connection.cursor()
    cursor.execute("""
           SELECT  OPERATION_ID,msg_in, msg_out
           FROM SYSREPODB.Z_ACH_OPERATION zao
           WHERE OPERATION_ID = 1482""",)
    OPERATION_ID, msg_in, msg_out = cursor.fetchone()
    jsonIn = json.loads(msg_in)
    jsonOut = json.loads(msg_out)
    print("OperationId {0}", OPERATION_ID)
    print("Msg In Id {0}", jsonIn['headerRQ']['msgId'])
    print("Msg Error code {0}", jsonOut['errorCode'])


main()
