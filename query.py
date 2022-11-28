import sqlite3
import pandas as pd

with sqlite3.connect("db/rugby.db") as conn:
    c = conn.cursor()
    query = input("Enter query: ")
    c.execute(query)
    columns = c.description
    result = c.fetchone()
    results = c.fetchall()

    print(pd.DataFrame(results, columns=columns))





