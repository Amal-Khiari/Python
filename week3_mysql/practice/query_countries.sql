SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.id) AS total_cities
FROM countries
JOIN cities ON countries.code = cities.country_code
GROUP BY countries.name
ORDER BY total_cities DESC;

SELECT cities.name, cities.population
FROM cities
JOIN countries ON cities.country_code = countries.code
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;