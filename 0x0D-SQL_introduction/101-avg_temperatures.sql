-- showing average temp in city oreder by average temp
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
