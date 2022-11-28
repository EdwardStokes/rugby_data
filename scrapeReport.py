from tools.writeToDb import write_fixture_performances_to_db

print("Enter URL:")
url = input()
print("Enter season or leave blank for 2022-2023 default:")
input_season = input()
season = input_season if input_season else "2022-2023"
write_fixture_performances_to_db(url, season)
