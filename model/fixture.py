from datetime import datetime


class Fixture:

    def __init__(self, name, date, fk_home_team_id, fk_away_team_id, home_score, away_score, fk_season_id):
        self.name = name
        self.date = datetime.strptime(date, "%A %d %B %Y")
        self.fk_home_team_id = fk_home_team_id
        self.fk_away_team_id = fk_away_team_id
        self.home_score = home_score
        self.away_score = away_score
        self.fk_season_id = fk_season_id
