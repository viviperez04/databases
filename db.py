
import cx_Oracle

connection = cx_Oracle.connect(user="viviana_perez", password="qX%NVLrF0pQa",
                               dsn="localhost/rds.test.integrator.co.ua.la")

cursor = connection.cursor()
cursor.execute("""
        SELECT *
        FROM SYSREPODB.Z_ACH_OPERATION zao
        WHERE DATETIME > TO_DATE('28/09/2021','DD/MM/YYYY')""",
               )
for operation_id, datetime, msg_in, msg_out in cursor:
    print("Values:", operation_id, datetime, msg_in, msg_out)