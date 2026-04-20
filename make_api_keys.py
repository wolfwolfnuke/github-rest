import sqlite3

my_db = sqlite3.connect("api.db")
db_cursor = my_db.cursor()
db_cursor.execute("CREATE TABLE IF NOT EXISTS api(key1" \
")")
while True:
    print("Type 1 for adding an api key. Type 2 to remove an api key. Type 3 to reset the api database")
    requested_action = input(">")
    if requested_action == "1":
        db_cursor.execute("INSERT INTO api VALUES('hi')")
    elif requested_action == "2":
        print("")
    elif requested_action == "3":
        print("resetting the database")
    elif requested_action == "4":
        db_cursor.execute("SELECT * FROM api")
        for row in db_cursor.fetchall():
            print(row)
    else:
        pass
    