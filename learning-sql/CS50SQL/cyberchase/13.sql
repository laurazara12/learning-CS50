/* In 13.sql, write a SQL query to explore a question of your choice. This query should:
Involve at least one condition, using WHERE with AND or OR */
SELECT title
FROM episodes
WHERE season = "5" OR season = "6"
ORDER BY title LIMIT 10;
