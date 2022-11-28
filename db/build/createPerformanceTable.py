import sqlite3

conn = sqlite3.connect('../rugby.db')
c = conn.cursor()
c.execute("""CREATE TABLE performance (
                name text,
                position text,
                fk_player_id integer,
                fk_team_id integer,
                fk_opponent_id integer,
                fk_fixture_id integer,
                fk_season_id,
                minutes integer,
                metres integer,
                carries integer,
                passes integer,
                tackles integer, 
                missed_tackles integer,
                turnovers_won integer,
                turnovers_conceded integer,
                defenders_beaten integer,
                assists integer,
                offloads integer,
                clean_breaks integer,
                lineout_wins integer,
                lineout_stolen integer
                )""")
conn.commit()
conn.close()
