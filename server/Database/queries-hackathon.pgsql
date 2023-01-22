
-- Query for Getting All Genres
SELECT genre, COUNT(mid) as movieCount
FROM genres
GROUP BY genre
ORDER BY count(mid) ASC;


--Query for best movie of a specific year
SELECT year, title, rating
FROM movies
WHERE year >= '2005-01-01' AND year <= '2005-12-31'
AND rating IS NOT NULL
ORDER BY rating DESC
LIMIT 10;

