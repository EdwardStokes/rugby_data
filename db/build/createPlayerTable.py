import sqlite3

conn = sqlite3.connect('../rugby.db')
c = conn.cursor()
c.execute("""CREATE TABLE player (
                name text,
                fk_team_id integer,
                dob string
                )""")
conn.commit()
conn.close()
