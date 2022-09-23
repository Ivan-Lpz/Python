SELECT cities.name, cities.population, cities.country_id FROM world.cities
JOIN world.countries ON cities.country_id = countries.id
WHERE countries.name = "Mexico" and cities.population > 500000
ORDER BY cities.population DESC;