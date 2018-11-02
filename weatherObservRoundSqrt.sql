SELECT ROUND(SQRT(POWER(MAX(lat_N) - MIN(lat_N), 2) + POWER(MAX(long_w) - MIN(long_w), 2)), 4)
FROM station;
