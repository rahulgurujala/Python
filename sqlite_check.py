from __future__ import print_function

import os
import sqlite3 as lite
import sys

# Script Name	: sqlite_check.py
# Author		: Craig Richards
# Created		: 20 May 2013
# Last Modified	:
# Version		: 1.0
# Modifications	:
# Description	: Runs checks to check my SQLITE database

dropbox = os.getenv("dropbox")
dbfile = "Databases\jarvis.db"
master_db = os.path.join(dropbox, dbfile)
con = None

try:
    con = lite.connect(master_db)
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    data = cur.fetchone()
    print(f"SQLite version: {data}")


except lite.Error as e:

    print(f"Error {e.args[0]}:")
    sys.exit(1)

finally:

    if con:
        con.close()

con = lite.connect(master_db)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
rows = cur.fetchall()
for row in rows:
    print(row)

con = lite.connect(master_db)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
while True:
    row = cur.fetchone()
    if row is None:
        break
    print(row[0])
