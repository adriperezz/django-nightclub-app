import psycopg2

#establishing the connection
conn = psycopg2.connect(
    user='adriperez',
    password='django',
    host='localhost',
    port= '8888'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# #Preparing query to create a database
# sql = '''CREATE database clubProject''';

# #Creating a database
# cursor.execute(sql)
# print("Database clubProject created successfully........")
