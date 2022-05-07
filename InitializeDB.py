import psycopg2

'''pip install psycopg2-binary'''

def initDB():
    
  # Establishing the connection
  conn = psycopg2.connect(database='inesctec', user='inesctec', password='inesctec', host='localhost', port='5432')
  # Creating a cursor object using the cursor() method
  cursor = conn.cursor()

  #Executing an SQL function using the execute() method
  cursor.execute("select version()")

  # Fetch a single row using fetchone() method.
  data = cursor.fetchone()
  print("Connection established to: ",data)

  # Create INFI Schema
  cursor.execute('CREATE SCHEMA IF NOT EXISTS "chargers"')
  
   # Create Fixed Variables table if doesn't exist
  cursor.execute('CREATE TABLE IF NOT EXISTS "fixedvars" ("id" SERIAL PRIMARY KEY, "instalationpower" INT, "numberchargers" INT, \
                 "powercost" INT, "occupancycost" INT)')

  # Commit changes
  conn.commit()

  # Closing the connection
  conn.close()