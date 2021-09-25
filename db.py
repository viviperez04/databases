import pyodbc
'''
Otros posibles nombres de servidores pueden ser
servidor = 'localhost\sqlexpress' # para casos específicos
servidor = 'miservidor,puerto' # para especificar un puerto alterno
'''
servidor = 'puerto:servidor.base.sql'  # Nombre del servidor SQL con el cual se hará la conexión
bddatos = 'mibdd'  # Nombre de la base de datos SQL
usuario = 'username' # Nombre del usuario de SQL
clave = 'clave'  # Contraseña del usuario de SQL
conn = pyodbc.connect('DRIVER={Controlador ODBC para el servidor SQL};
                       SERVER='+servidor+';
                       DATABASE='+bddatos+';
                       UID='+usuario+';
                       PWD='+clave)
'''
pyodbc.connect() inicia la conexión con el servidor SQL
tomando como argumentos, en orden,:
- El nombre del controlador SQL
- El servidor al cual se hará la conexión
- El nombre de la Base de datos que será consultada
- El nombre de usuario que tiene acceso a la base de datos
- La contraseña del usuario que accede a la base de datos
'''
cursor = conn.cursor() # se crea el cursor para la conexión