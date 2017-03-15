# python 3

import os
import sys
import sqlite3

try:
    log_file = str(sys.argv[1])
except IndexError:
    print ("")
    print ("usage: python3 log2db.py [txt_file]")
    print ("")
    sys.exit(0)

open_file = open(log_file, "r")

query_values = []

for line in open_file.readlines():
    t =  line.split(" ")[0], \
            line.split(" ")[1], \
            line.split(" ")[3], \
            line.split(" ")[6], \
            line.split(" ")[8]
    query_values.append(t)

open_file.close()

conn = sqlite3.connect("database/dns.sqlite3")

conn.executemany("INSERT INTO queries "
                "(query_date, query_time, query_src, query_type, query) "
                "VALUES (?,?,?,?,?)", query_values)

conn.commit()

conn.close()