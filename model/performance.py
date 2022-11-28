class Performance:

    def __init__(self, stats_line, fk_player_id, fk_team_id, fk_opponent_id, fk_fixture_id, fk_season_id):
        self.name = stats_line[1]
        self.position = stats_line[0]
        self.fk_player_id = fk_player_id
        self.fk_team_id = fk_team_id
        self.fk_opponent_id = fk_opponent_id
        self.fk_fixture_id = fk_fixture_id
        self.fk_season_id = fk_season_id
        self.minutes = None if stats_line[15] == "-" else int(stats_line[15])
        self.metres = None if stats_line[2] == "-" else int(stats_line[2])
        self.carries = None if stats_line[3] == "-" else int(stats_line[3])
        self.passes = None if stats_line[4] == "-" else int(stats_line[4])
        self.tackles = None if stats_line[5] == "-" else int(stats_line[5])
        self.missed_tackles = None if stats_line[6] == "-" else int(stats_line[6])
        self.turnovers_won = None if stats_line[7] == "-" else int(stats_line[7])
        self.turnovers_conceded = None if stats_line[8] == "-" else int(stats_line[8])
        self.defenders_beaten = None if stats_line[9] == "-" else int(stats_line[9])
        self.assists = None if stats_line[10] == "-" else int(stats_line[10])
        self.offloads = None if stats_line[11] == "-" else int(stats_line[11])
        self.clean_breaks = None if stats_line[12] == "-" else int(stats_line[12])
        self.lineouts_won = None if stats_line[13] == "-" else int(stats_line[13])
        self.lineouts_stolen = None if stats_line[14] == "-" else int(stats_line[14])

