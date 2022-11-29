import pyodbc
server = 'rekdatserver.database.windows.net'
database = 'database'
username = 'serveradminlogin'
password = '{Rangga12!}'   
driver= '{ODBC Driver 17 for SQL Server}'

def run_twitter_load():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+
        server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            #Query to be executed
            cursor.execute("INSERT INTO [dbo].[tabletext](text) VALUES ('xxxxxxx')")

run_twitter_load()