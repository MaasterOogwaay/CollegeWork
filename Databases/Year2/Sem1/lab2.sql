/* setup */
DROP DATABASE IF EXISTS lab1SQL;
CREATE DATABASE IF NOT EXISTS lab1SQL;
USE lab1SQL;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS details;


CREATE TABLE DETAILS (
	id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
	firstName VARCHAR(15) NOT NULL,
	lastName VARCHAR(20) NOT NULL,
	age INTEGER NOT NULL,
	gender VARCHAR(1) NOT NULL,
	position VARCHAR(15) NOT NULL,
	department VARCHAR(20) NOT NULL,
	rate DECIMAL(7, 2) NOT NULL,
	hours INTEGER NOT NULL);

SELECT 'INSERTING DATA INTO DATABASE' as 'INFO';

INSERT INTO details VALUES ( null, 'Joe', 'Mullins', 64, 'M', 'Lecturer', 'Engineering', 63.08, 12);
INSERT INTO details VALUES ( null, 'Joan', 'Macgill', 27, 'F', 'Researcher', 'Science', 38, 35);
INSERT INTO details VALUES ( null, 'Jim', 'Mitchell', 51, 'M', 'Researcher', 'Business', 38, 25);
INSERT INTO details VALUES ( null, 'John', 'Magner', 47, 'M', 'Lecturer', 'Humanities', 63.08, 16);
INSERT INTO details VALUES ( null, 'Jean', 'Madden', 45, 'F', 'Professor', 'Design', 76.45, 14);
INSERT INTO details VALUES ( null, 'Jack', 'Minogue', 61, 'M', 'Administrator', 'Hospitality', 45.57, 37);
INSERT INTO details VALUES ( null, 'Josephine', 'Mahony', 33, 'F', 'Head', 'Nursing', 98.56, 40);
INSERT INTO details VALUES ( null, 'Juan', 'Mosley', 56, 'M', 'Professor', 'Engineering', 76.45, 11);
INSERT INTO details VALUES ( null, 'Jamie', 'Mulllen', 45, 'M', 'Researcher', 'Science', 38, 37);
INSERT INTO details VALUES ( null, 'Julie', 'Mooney', 39, 'F', 'Lecturer', 'Business', 63.08, 18);
INSERT INTO details VALUES ( null, 'Jane', 'Mccarthy', 37, 'F', 'Administrator', 'Design', 45.57, 45);
INSERT INTO details VALUES ( null, 'James', 'May', 38, 'M', 'Researcher', 'Hospitality', 38, 9);
INSERT INTO details VALUES ( null, 'Joseph', 'Manning', 32, 'M', 'Lecturer', 'Hospitality', 63.08, 16);
INSERT INTO details VALUES ( null, 'Judith', 'Milner', 36, 'F', 'Lecturer', 'Nursing', 63.08, 20);
INSERT INTO details VALUES ( null, 'Jerome', 'Murphy', 26, 'M', 'Head', 'Engineering', 98.56, 42);
INSERT INTO details VALUES ( null, 'Jude', 'Manley', 28, 'M', 'Head', 'Science', 98.56, 41);
INSERT INTO details VALUES ( null, 'Juanita', 'Mahon', 59, 'F', 'Administrator', 'Engineering', 45.57, 49);
INSERT INTO details VALUES ( null, 'Justin', 'Maguire', 25, 'M', 'Lecturer', 'Business', 63.08, 16);
INSERT INTO details VALUES ( null, 'Jacqulinen', 'Musgrave', 43, 'F', 'Professor', 'Business', 76.45, 10);
INSERT INTO details VALUES ( null, 'Julia', 'Moore', 36, 'F', 'Administrator', 'Science', 45.57, 38);

SELECT 'CHECKING TO SEE IF EVERYTHING WORKED' as 'INFO';

SELECT * from details;

/* select certain columns */
select firstName, lastName from details;

/* distinct number of groups */
select distinct gender from details;

/* rename column for readability */
select distinct rate as cost from details;

/* return data with certain query */
select * from details where gender = "F";

/* other predicates */
- and
- or 
- not

/* order in which data is outputted (ascending) */
select * from details order by lastName;

/* order in which data is outputted (descending) */
select * from details order by lastName desc;

/* multiple ordering */
select * from details order by department desc, position asc;

/* calculations within expression */
select *, (65 - age) as yearToRetire from details; /* only in result. Not saved to database */

/* between operator */
select * from details where age between 40 and 50;

/* like operator selects values with a particular pattern */
/* the % is a wildcard so the query looks for anything that matches */
select * from details where lastName like "%an%";

/* all people whose lastName ended with n */
select * from details where lastName like "%n";

/* use "_" to mask certain characters */
/* all records where the 2nd last letter in lastName is 3 */
select * from details where lastName like "%e_";

/* Aggregration Functions */
- Count
- Avg
- Max
- Min
- Sum

/* num of rows in table */
select count(*) from details;
select count(*) from details where position = "Lecturer";

/* average of values from column */
select avg(age) as averageAge from details;
select avg(age) from details where age >= 50;

/* min/max determines min/max from column */
select min(age) as youngest from details;
select max(age) as oldest from details;

/* determines sum of values within column */
select sum(rate*hours) as totalWageBill from details;

/* Exercises */
select * from details where department = "Engineering";
select * from details where position = "Administrator";
select * from details where id > 17;
select * from details where age > 46;
select * from details where position = "Lecturer";
select distinct rate from details;
select distinct department from details;
select distinct position from details;
select distinct position as jobs from details;
select firstName, lastName, age, gender from details where position = "Lecturer" and age > 40;
select firstName, lastName, age, gender from details where position = "Lecturer" and age >= 35 and age <= 50;
/* v1 */ select * from details where gender = "F" and position = "Lecturer" or gender = "F" and position = "Professor";
/* v2 */ select * from details where gender = "F" and (position = "Lecturer" or position = "Professor");
select * from details order by age desc; 
select * from details where gender = "F" order by firstName;
select * from details where gender = "M" order by firstName;
select * from details where position = "Lecturer" order by firstName;

select *, (rate * hours) as weeklyWage from details;

select * from details where (id % 2 = 0);