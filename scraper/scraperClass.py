from requests_html import HTMLSession


class Scraper:
    def __init__(self, url):
        self.url = url
        self.session = HTMLSession()
        self.r = self.session.get(self.url)
        self.home_table = []
        self.away_table = []
        self.starters_tag = ""
        self.replacements_tag = ""
        self.date = ""
        self.home_team = ""
        self.away_team = ""
        self.home_score = ""
        self.away_score = ""
        self.home_stats = []
        self.away_stats = []
        self.render_html()
        self.set_rendered_attrs()
        self.set_match_info()
        self.set_team_stats()
        self.set_score()

    def render_html(self):
        self.r.html.render(sleep=1, keep_page=True, timeout=50)

    def scrape_date(self):
        return self.r.html.find(".match__scoreboard-date")[0].text

    def scrape_teams(self):
        tab = self.r.html.find(".match-performance__nav")
        spans = tab[0].find('span')
        return [spans[0].text, spans[1].text]

    def scrape_score(self):
        return self.r.html.find(".match__full-time")[0].text

    # # not used?
    # def scrape_data_headers(self):
    #     t_headers = self.r.html.find('thead')
    #     data_headers = t_headers[1].text.split("\n")
    #     return data_headers

    @staticmethod
    def scrape_player_data(table, td_class):
        container = []
        for row in table.find("tr"):
            player_data = row.find(td_class)
            for d in player_data:
                scraped_data = d.text.split("\n")
                is_sub = int(scraped_data[0]) > 15
                spans = d.find("span")
                if len(spans) > 1:
                    player = spans[0].text
                    replacement = spans[2].text
                    scraped_data[1] = player
                    minutes = spans[3].text.rstrip("'") if not is_sub else 80 - int(spans[3].text.rstrip("'"))
                    scraped_data.extend([minutes, replacement])
                    container.append(scraped_data)
                else:
                    scraped_data.extend(["-", "-"]) if is_sub else scraped_data.extend(["80", "-"])
                    container.append(scraped_data)
        return container

    def scrape_home_stats(self):
        starters = self.scrape_player_data(self.home_table, self.starters_tag)
        replacements = self.scrape_player_data(self.home_table, self.replacements_tag)
        full_team = starters + replacements
        return full_team

    def scrape_away_stats(self):
        starters = self.scrape_player_data(self.away_table, self.starters_tag + "--b")
        replacements = self.scrape_player_data(self.away_table, self.replacements_tag + "--b")
        full_team = starters + replacements
        return full_team

    def set_rendered_attrs(self):
        self.home_table = self.r.html.find("table")[1]
        self.away_table = self.r.html.find("table")[2]
        self.starters_tag = ".compare-table__players"
        self.replacements_tag = ".compare-table__replacements"

    def set_match_info(self):
        self.date = self.scrape_date()
        self.home_team, self.away_team = self.scrape_teams()

    def set_team_stats(self):
        for row in self.scrape_home_stats():
            self.home_stats.append(row)

        for row in self.scrape_away_stats():
            self.away_stats.append(row)

    def set_score(self):
        self.home_score, self.away_score = self.scrape_score().split(" - ")

    def get_date(self):
        return self.date

    def get_teams(self):
        return [self.home_team, self.away_team]

    def get_home_team(self):
        return self.home_team

    def get_away_team(self):
        return self.away_team

    def get_fixture_name(self):
        return f"{self.home_team} V {self.away_team} - {self.date}"

    def get_home_stats(self):
        return self.home_stats

    def get_away_stats(self):
        return self.away_stats

    def get_home_score(self):
        return self.home_score

    def get_away_score(self):
        return self.away_score

