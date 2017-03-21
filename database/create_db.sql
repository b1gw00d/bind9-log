CREATE TABLE "queries" (
	`query_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`query_date`	TEXT NOT NULL,
	`query_time`	TEXT NOT NULL,
	`query_src`	TEXT NOT NULL,
	`query_type`	TEXT,
	`query`	TEXT NOT NULL
)