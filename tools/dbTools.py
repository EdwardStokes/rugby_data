from model.fixture import Fixture
from model.player import Player
from model.season import Season
from model.team import Team


def check_team_exists(conn, team_name):
    c = conn.cursor()
    c.execute("SELECT name FROM team WHERE name = :name", {'name': team_name})
    if not c.fetchone():
        return False
    return True


def add_team(conn, team_name):
    c = conn.cursor()
    row = Team(team_name)
    c.execute("INSERT INTO team VALUES (:name)", {'name': row.name})
    conn.commit()


def get_team_pk(conn, team_name):
    c = conn.cursor()
    c.execute("SELECT rowid FROM team WHERE name = :team_name", {'team_name': team_name})
    return c.fetchone()[0]


def check_player_exists(conn, player_name, team_fk):
    c = conn.cursor()
    c.execute("SELECT name FROM player WHERE name = :player_name AND fk_team_id = :team_fk",
              {"player_name": player_name, "team_fk": team_fk})
    if c.fetchone():
        return True
    return False


def add_player(conn, player_name, team_fk):
    row = Player(player_name, team_fk)
    c = conn.cursor()
    c.execute("INSERT INTO player VALUES (:name, :fk_team_id, :dob)", {"name": row.name,
                                                                       "fk_team_id": row.fk_team_id,
                                                                       "dob": row.dob})
    conn.commit()


def get_player_pk(conn, player_name, team_fk):
    c = conn.cursor()
    c.execute("SELECT rowid FROM player WHERE name = :player_name AND fk_team_id = :team_fk",
              {"player_name": player_name, "team_fk": team_fk})
    return c.fetchone()[0]


def check_season_exists(conn, season_name):
    c = conn.cursor()
    c.execute("SELECT name FROM season WHERE name = :season_name",
              {"season_name": season_name})
    if c.fetchone():
        return True
    return False


def add_season(conn, season_name):
    row = Season(season_name)
    c = conn.cursor()
    c.execute("INSERT INTO season VALUES (:name)", {"name": row.name})
    conn.commit()


def get_season_pk(conn, season_name):
    c = conn.cursor()
    c.execute("SELECT rowid FROM season WHERE name = :season_name",
              {"season_name": season_name})
    return c.fetchone()[0]


def check_fixture_exists(conn, fixture_name):
    c = conn.cursor()
    c.execute("SELECT name FROM fixture WHERE name = :fixture_name", {'fixture_name': fixture_name})
    if not c.fetchone():
        return False
    return True


def add_fixture(conn, scraper, season_id):
    row = Fixture(scraper.get_fixture_name(), scraper.get_date(), scraper.get_home_team(), scraper.get_away_team(),
                  scraper.get_home_score(), scraper.get_away_score(), season_id)
    c = conn.cursor()
    c.execute("""INSERT INTO fixture VALUES (:name, :date, :fk_home_team_id, :fk_away_team_id, :home_score,
               :away_score, :fk_season_id)""",
              {"name": row.name, "date": row.date, "fk_home_team_id": row.fk_home_team_id,
               "fk_away_team_id": row.fk_away_team_id, "home_score": row.home_score, "away_score": row.away_score,
               "fk_season_id": row.fk_season_id})
    conn.commit()


def get_fixture_pk(conn, fixture_name):
    c = conn.cursor()
    c.execute("SELECT rowid FROM fixture WHERE name = :fixture_name",
              {"fixture_name": fixture_name})
    return c.fetchone()[0]


def check_performance_exists(conn, player_fk, team_fk, fixture_fk):
    c = conn.cursor()
    c.execute("""SELECT rowid from performance WHERE fk_player_id = :player_fk AND fk_team_id = :team_fk AND
    fk_fixture_id = :fixture_fk""", {"player_fk": player_fk, "team_fk": team_fk, "fixture_fk": fixture_fk})
    if not c.fetchone():
        return False
    return True


def add_performance(conn, performance):
    c = conn.cursor()
    c.execute("""INSERT INTO performance VALUES (:name, :position, :player_id, :team_id, :opponent_id, :fixture_id, 
              :season_id, :minutes, :metres, :carries, :passes, :tackles, :missed_tackles, :turnovers_won, 
              :turnovers_conceded, :defenders_beaten, :assists, :offloads, :clean_breaks, :lineouts_won, 
              :lineouts_stolen)""",
              {"name": performance.name, "position": performance.position, "player_id": performance.fk_player_id,
               "team_id": performance.fk_team_id, "opponent_id": performance.fk_opponent_id,
               "fixture_id": performance.fk_fixture_id, "season_id": performance.fk_season_id, "minutes": performance.minutes, "metres": performance.metres,
               "carries": performance.carries, "passes": performance.passes, "tackles": performance.tackles,
               "missed_tackles": performance.missed_tackles, "turnovers_won": performance.turnovers_won,
               "turnovers_conceded": performance.turnovers_conceded,
               "defenders_beaten": performance.defenders_beaten, "assists": performance.assists,
               "offloads": performance.offloads, "clean_breaks": performance.clean_breaks,
               "lineouts_won": performance.lineouts_won, "lineouts_stolen": performance.lineouts_stolen
               })
    conn.commit()


def check_performances_exists(conn, fixture):
    c = conn.cursor()
    c.execute("SELECT fixture_id FROM fixture WHERE fixture_id = :fixture", {'fixture': fixture})
    if not c.fetchone():
        return False
    return True
