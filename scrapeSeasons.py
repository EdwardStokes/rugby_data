from tools.writeToDb import write_fixture_performances_to_db
from tools.scrapingTools import get_match_report_urls


season_names = ["2014-2015", "2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021",
                "2021-2022", "2022-2023"]
targets = []

for season_name in season_names:
    print(f"Scrape {season_name}? Enter 'Yes' to add to list:")
    if input().lower() in ["yes", "y"]:
        targets.append(season_name)

for season_name in targets:
    report_urls = get_match_report_urls(season_name)
    for report_url in report_urls:
        write_fixture_performances_to_db("https://www.premiershiprugby.com/" + report_url, season_name)
