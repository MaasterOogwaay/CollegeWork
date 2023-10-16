/* Find all countries beginning with Z */
select name from country
where name like "Z%";

-- Find the names and populations of all countries in Europe beginning with ‘A’.
select name, population from country
where continent = "Europe"
and name like "A%";

-- Find the names and populations of the 10 most populated countries
select name, population from country order by population desc limit 10;

-- Find all countries where Italian is spoken
select name, language from country 
inner join countrylanguage on CountryCode = Code
where language = "Italian";

-- Find all countries where German is spoken and is official
select name, language from country 
inner join countrylanguage on CountryCode = Code
where language = "German"
and isOfficial = True;

-- Find the city names and populations in China with over 3 million in population
select name, population from city
where CountryCode = "CHN"
and population > 3000000;

select city.name, city.population from city
inner join country on (CountryCode = Code)
where country.name = "China" 
and city.population > 3000000;

-- Find the total number of countries in each continent
select continent, count(*) as numOfCountries
from country
group by continent;

-- Write an INTERSECT SQL query that returns a list of languages common to China and Malaysia
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "China"
intersect
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "Malaysia";

-- Write an EXCEPT SQL query that returns a list of the languages spoken in Singapore but not in China
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "Singapore"
except
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "China";

-- Write a UNION SQL query that returns a list containing Japan and all it’s languages
(select name from country where name = "Japan")
UNION
(select language from countryLanguage inner join country on(CountryCode = Code)
where country.name = "Japan");

