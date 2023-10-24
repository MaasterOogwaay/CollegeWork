-- return the total number of countries with no head of state
select count(HeadOfState) as "total" from country
where HeadOfState = "";

-- return the total number of regions in South America
select count(distinct region) as "Number of Regions" from country
where region = "South America";

-- return the total number of countries Queen "Elisabeth II" is head of state of.
select count(HeadOfState) as "total" from country
where HeadOfState = "Elisabeth II";

-- return the total number of regions in Europe
select count(distinct region) as "Number of Regions" from country
where continent = "Europe";

-- return the total number of countries that have a republic as their government format
select count(*) as "Total Republics" from country 
where GovernmentForm = "Republic";

--  return the average life expectancy on the continent of Oceania
select avg(LifeExpectancy) as "Life expectancy" from country 
where continent = "Oceania";

--  return a list of countries without any population
select name from country 
where population <= 0;

--  return the total number of regions in Antarctica.
select count(distinct region) as "Number of Regions" from country
where continent = "Antarctica";

-- return the total number of continents in the world
select count(distinct continent) as "Number of Continents" from country;

-- return the average life expectancy on the continent of Europe
select avg(LifeExpectancy) as "Life expectancy" from country 
where continent = "Europe";

-- return the number of cities in the United States
select country.name, count(city.name) as "Total Cities" 
from country, city 
where (CountryCode = Code) 
and country.name = "United States"; 

-- return a list of the top 5 most populated cities in the world along with the the name of the country they belong to
select country.name as "Country", city.name as "City", city.population from city, country
where (CountryCode = Code)
order by population desc limit 5;

--  return the number of people in the United States whose official language is English
select name, language, isOfficial, percentage, population, sum(percentage*population) as "English Speakers"
from countryLanguage, country
where (CountryCode = Code)
and country.name = "United States"
and isOfficial = "T"
group by name, language, isOfficial, percentage, population;


-- return a list of the number of official languages spoken on each continent
select continent, count(distinct language) as "Total"
from country, countryLanguage
where (CountryCode = Code)
and isOfficial = "T"
group by continent;

--  return the number of people in the United States whose language is NOT English
select name, language, isOfficial, percentage, population, round(sum((100-percentage)*population),2) as "English Speakers"
from countryLanguage, country
where (CountryCode = Code)
and country.name = "United States"
and isOfficial = "T"
group by name, language, isOfficial, percentage, population;


-- EXCEPT SQL query that would return a list of those languages that are NOT common to both Australia and the United States
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "Australia"
except
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.name = "United States";

-- INTERSECT SQL query that would return a list of those languages that are common to both North and South America
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.continent = "North America"
intersect
select language 
from countryLanguage inner join country on (CountryCode = Code)
where country.continent = "South America";

-- UNION SQL query that would return a list containing Ireland and its cities including the number of inhabitants
(select country.name as "Details", country.population as "Inhabitants" 
from country where name = "Ireland")
union 
(select city.name, city.population from city, country 
where code = CountryCode 
and country.name = "Ireland");
