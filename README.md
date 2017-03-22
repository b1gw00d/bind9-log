# Convert bind9 queries log to html or sqlite3 db

## Prerequisites:
    python 3.x
    jinja2 (only for log2html.py)

## Usage:
    HTML:
    
        python3 log2html.py [query log file] [output html file]
       

    SQLite3:

        sqlite3 database_name
        sqlite> .read database/create_db.sql
        python3 log2db.py [query log file] [output db]