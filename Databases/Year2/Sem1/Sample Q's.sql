-- Return a list of the regions in Oceania
select distinct region from country where continent = "Oceania";

-- Return the total number of regions in Africa
select count(distinct region) as "Number of Regions" from country where continent = "africa";

-- name of the city with the smallest population
select name, population from city 
where population = (select min(population) from city);

-- total number of official languages in the world
select count(distinct language) as "Unique Languages" from countryLanguage where isOfficial = true;

-- returns the number of cities in the US
select country.name, count(city.name) as "Total Cities" 
from country, city 
where (CountryCode = Code) 
and country.name = "United States"; 

-- return a list of official languages in Ireland
select name, language, isOfficial 
from country, countryLanguage
where (CountryCode = Code)
and name = "Ireland"
and isOfficial = true;

-- UNION | return a list containing Belgium and it's official languages
(select name as "Details" from country where name = "Belgium")
UNION
(select language from countryLanguage 
inner join country on (CountryCode = Code)
where country.name = "Belgium");

-- INTERSECT | return a list of languages common to Austrailia and US
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "Australia"
intersect
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "United States";

-- EXCEPT | return a list of languages not common to Austrailia and US
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "Australia"
except
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "United States";
