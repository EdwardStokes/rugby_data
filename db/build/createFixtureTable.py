import sqlite3

conn = sqlite3.connect('../rugby.db')
c = conn.cursor()
c.execute("""CREATE TABLE fixture (
                name text,
                date text,
                fk_home_team_id integer,
                fk_away_team_id integer,
                home_score integer,
                away_score integer,
                fk_season_id integer
                )""")
conn.commit()
conn.close()
