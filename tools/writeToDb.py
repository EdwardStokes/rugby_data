from tools import dbTools as Tools
from scraper.scraperClass import Scraper
from time import sleep
from model.performance import Performance
import sqlite3


def write_team_performances_to_db(conn, performances, team_fk, opposition_fk, fixture_fk, season_fk):
    for performance in performances:
        player_name = performance[1]
        # CHECK PLAYER AND ADD IF NOT IN DB
        if not Tools.check_player_exists(conn, player_name, team_fk):
            print(f"Adding player {player_name} to db.")
            Tools.add_player(conn, player_name, team_fk)
        player_fk = Tools.get_player_pk(conn, player_name, team_fk)
        row = Performance(performance, player_fk, team_fk, opposition_fk, fixture_fk, season_fk)
        # CHECK PERFORMANCE AND ADD IF NOT IN DB
        if not Tools.check_performance_exists(conn, row.fk_player_id, row.fk_team_id, row.fk_fixture_id):
            print(f"Adding performance {player_name} - fixture ID:f{row.fk_fixture_id} to db.")
            Tools.add_performance(conn, row)


def write_fixture_performances_to_db(report_url, season_name):
    try:
        sleep(7)
        scraper = None
        scraper = Scraper(report_url)
        path = "db/rugby.db"
        fixture_name = scraper.get_fixture_name()
        team_names = scraper.get_teams()
        with sqlite3.connect(path) as conn:
            # CHECK TEAM AND ADD IF NOT IN DB
            for team_name in team_names:
                if not Tools.check_team_exists(conn, team_name):
                    print(f"Adding team {team_name} to db.")
                    Tools.add_team(conn, team_name)
            # CHECK SEASON AND ADD IF NOT IN DB
            if not Tools.check_season_exists(conn, season_name):
                print(f"Adding season {season_name} to db.")
                Tools.add_season(conn, season_name)
            season_fk = Tools.get_season_pk(conn, season_name)
            # CHECK FIXTURE AND ADD IF NOT IN DB
            if not Tools.check_fixture_exists(conn, fixture_name):
                print(f"Adding fixture {fixture_name} to db.")
                Tools.add_fixture(conn, scraper, season_fk)

            fixture_fk = Tools.get_fixture_pk(conn, fixture_name)
            home_team_name = scraper.get_home_team()
            home_team_fk = Tools.get_team_pk(conn, home_team_name)
            away_team_name = scraper.get_away_team()
            away_team_fk = Tools.get_team_pk(conn, away_team_name)
            home_performances = scraper.get_home_stats()
            away_performances = scraper.get_away_stats()
           # CHECK PERFORMANCES AND ADD IF NOT IN DB
            write_team_performances_to_db(conn, home_performances, home_team_fk, away_team_fk, fixture_fk, season_fk)
            write_team_performances_to_db(conn, away_performances, away_team_fk, home_team_fk, fixture_fk, season_fk)

            scraper.session.close()
    except Exception as e:
        print(f"ERROR SCRAPING DATA FROM {report_url}, DUMMY.")
        print(e)
        if scraper:
            scraper.session.close()
