import pyodbc
from twitter_extract import run_twitter_extract
from twitter_transform import run_twitter_transform
server = 'fastserver.database.windows.net'
database = 'fast_database'
username = 'serveradminlogin'
password = '{Rangga12!}'   
driver= '{ODBC Driver 17 for SQL Server}'

raw = run_twitter_extract()
cleaned = run_twitter_transform(raw)

def run_twitter_load():
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+
        server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            #Query to be executed
            for i in range(cleaned.shape[0]):
                cursor.execute("INSERT INTO [dbo].[tabletext](text) VALUES ('{0}')".format(cleaned.iloc[i]['text']))

run_twitter_load()