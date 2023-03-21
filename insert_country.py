import json
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="aggamedb",
    user="aggame",
    password="?!aggame"
)

# Create a cursor object
cur = conn.cursor()


with open('countryCodes.json', 'r') as f:
    data = json.load(f)

# Insert the data into the table
for country in data:
    name = country['name']
    dial_code = country['dial_code']
    code = country['code']
    flag = country['flag']
    cur.execute("""
        INSERT INTO general_settings (country_name, country_dial_code, country_short_name, country_flag)
        VALUES (%s, %s, %s, %s);
    """, (name, dial_code, code, flag))

# Commit the transaction and close the connection
conn.commit()
conn.close()
