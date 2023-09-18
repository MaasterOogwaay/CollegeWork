/* Lab 1 - SQL Introduction */

/* List the databases present */
show databases;

/* List the tables in the information_schema database */
show tables from information_schema;

/* Show schema for the user_privileges table in the information_schema database */
describe information_schema.user_privileges;

/* Change the current database to information_schema */
use information_schema;

/* Show schema for the user_privileges table in the information_schema database */
describe user_privileges;

/* Same as previous command */
show columns from user_privileges;
 
/* List the contents of the user_privileges table */
select *
from user_privileges;

/* Create a database called myTest and change to that database */
create database myTest;

/* Create a table called my_info */
create table my_info
(
	id integer not null,
	first_name char(12),
	last_name char(20),
	gender char(1)
);

/* Show table schema for my_info */
describe my_info;

/* Show all the data in the table */
select *
from my_info;

/* Add data to the table */
insert into my_info(id, first_name, last_name, gender) values(1, 'Joe', 'Bloggs', 'M');

/* Quick way to insert data */
insert into my_info values(2, 'Jane', 'Doe', 'F');

/* Using null values in insert */
insert into my_info values (3, 'John', 'Murphy', null);

/* Delete table and all the data */
drop table my_info;

/* Delete all the females */
delete from my_info
where gender = 'F';

/* Deleting using nulls is a special case - use 'is' */
delete from my_info
where gender is null;

/* Delete the data but leave the table */
delete from my_info;

/* Lab 1 - Create a database */
create table details(
	id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
	firstname VARCHAR(15) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	age INTEGER NOT NULL,
	gender VARCHAR(1) NOT NULL,
	position VARCHAR(15) NOT NULL,
	department VARCHAR(20) NOT NULL,
	rate DECIMAL(7, 2) NOT NULL,
	hours INTEGER NOT NULL
);

INSERT INTO details VALUES(null, 'Joe', 'Mullins', 64, 'M', 'Lecturer', 'Engineering', 63.08, 12);
INSERT INTO details VALUES(null, 'Joan', 'Macgill', 27, 'F', 'Researcher', 'Science', 38.00, 35);
INSERT INTO details VALUES(null, 'Jim', 'Mitchell', 51, 'M', 'Researcher', 'Business', 38.00, 25);
INSERT INTO details VALUES(null, 'John', 'Magner', 47, 'M', 'Lecturer', 'Humanities', 63.08, 16);
INSERT INTO details VALUES(null, 'Jean', 'Madden', 45, 'F', 'Professor', 'Design', 76.45, 14);
INSERT INTO details VALUES(null, 'Jack', 'Minogue', 61, 'M', 'Administrator', 'Hospitality', 45.57, 37);
INSERT INTO details VALUES(null, 'Josephine', 'Mahoney', 33, 'F', 'Head', 'Nursing', 98.56, 40);
INSERT INTO details VALUES(null, 'Juan', 'Mosley', 56, 'M', 'Professor', 'Engineering', 76.45, 11);
INSERT INTO details VALUES(null, 'Jamie', 'Mullen', 45, 'M', 'Researcher', 'Science', 38.00, 37);
INSERT INTO details VALUES(null, 'Julie', 'Mooney', 39, 'F', 'Lecturer', 'Business', 63.08, 18);
INSERT INTO details VALUES(null, 'Jane', 'McCarthy', 37, 'F', 'Administrator', 'Design', 45.57, 45);
INSERT INTO details VALUES(null, 'James', 'May', 38, 'M', 'Researcher', 'Hospitality', 38.00, 16);
INSERT INTO details VALUES(null, 'Joseph', 'Manning', 32, 'M', 'Lecturer', 'Hospitality', 63.08, 16);
INSERT INTO details VALUES(null, 'Judith', 'Milner', 36, 'F', 'Lecturer', 'Nursing', 63.08, 20);
INSERT INTO details VALUES(null, 'Jerome', 'Murphy', 26, 'M', 'Head', 'Engineering', 98.56, 42);
INSERT INTO details VALUES(null, 'Jude', 'Manley', 28, 'M', 'Head', 'Science', 98.56, 42);
INSERT INTO details VALUES(null, 'Juanita', 'Mahon', 59, 'F', 'Administrator', 'Engineering', 45.57, 49);
INSERT INTO details VALUES(null, 'Justin', 'Maguire', 25, 'M', 'Lecturer', 'Business', 63.08, 16);
INSERT INTO details VALUES(null, 'Jaculinen', 'Musgrave', 43, 'F', 'Professor', 'Business', 76.45, 10);
INSERT INTO details VALUES(null, 'Julia', 'Mullins', 64, 'F', 'Lecturer', 'Engineering', 63.08, 12);
INSERT INTO details VALUES(null, 'Joe', 'Moore', 36, 'F', 'Administrator', 'Science', 45.57, 38);