SELECT city, LENGTH(city)
FROM station
GROUP BY city
ORDER BY LENGTH(city)
LIMIT 1;
SELECT city, LENGTH(city)
FROM station
GROUP BY city
ORDER BY LENGTH(city) DESC
LIMIT 1;
