import sqlite3

conn = sqlite3.connect('../rugby.db')
c = conn.cursor()
c.execute("""CREATE TABLE season (
                name text
                )""")
conn.commit()
conn.close()
