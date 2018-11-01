SELECT co.continent, ROUND(AVG(c.population) - 0.5)
FROM city c
JOIN country co
ON c.countrycode = co.code
GROUP BY co.continent;
