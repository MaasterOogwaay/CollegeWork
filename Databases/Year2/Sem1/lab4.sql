DROP DATABASE IF EXISTS library;
CREATE DATABASE IF NOT EXISTS library;
USE library;

SELECT 'CREATING EMPLOYEE TABLE' as 'INFO';

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
	emp_id INTEGER AUTO_INCREMENT ,
	firstName VARCHAR(15) NOT NULL,
	lastName VARCHAR(20) NOT NULL,
	address1 VARCHAR(20) NOT NULL,
	address2 VARCHAR(20),
	town VARCHAR(20),
	contactNo VARCHAR(15) NOT NULL,
	dateOfBirth DATETIME NOT NULL,
	gender VARCHAR(1) NOT NULL,
	position VARCHAR(15) NOT NULL,
	rate DECIMAL(7, 2) NOT NULL,
	PRIMARY KEY(emp_id) );
	
SELECT 'INSERTING DATA INTO TABLE EMPLOYEE' as 'INFO';

INSERT INTO employees VALUES ( null, 'Joe', 'Mullins', 'Big long Road',null, 'Athlone', '08712345678', '1980-12-21', 'M', 'Manager', 24.99);
INSERT INTO employees VALUES ( null, 'Derek', 'Smith', '65 Elm Rd','Retreat', 'Athlone','08553737873', '1995-03-19', 'M', 'Trainee', 8.99);
INSERT INTO employees VALUES ( null, 'Carol', 'Long', 'Arcadia',null, 'Athlone', '0878998766', '1985-04-30', 'F', 'Supervisor', 18.99);
INSERT INTO employees VALUES ( null, 'Mike', 'Adams', '36 Bloomfied Drive','Coosan', 'Athlone', '08515432678', '1992-12-21', 'M', 'Employee', 13.50);
INSERT INTO employees VALUES ( null, 'Maura', 'Jones', 'The Bog',null, 'Clara', '0877897897', '1990-12-21', 'F', 'Employee', 13.50);
INSERT INTO employees VALUES ( null, 'Treasa', 'Cummins', 'Cam', 'Curry', 'Brideswell', '0876534276', '1978-02-14', 'F', 'Employee', 13.50);

SELECT 'CHECKING TO SEE IF DATA INSERTED TO EMPLOYEES CORRECTLY' as 'INFO';

SELECT * FROM employees;


SELECT 'CREATING CUSTOMERS TABLE' as 'INFO';

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
	cus_id INTEGER AUTO_INCREMENT ,
	firstName VARCHAR(15) NOT NULL,
	lastName VARCHAR(20) NOT NULL,
	address1 VARCHAR(20) NOT NULL,
	address2 VARCHAR(20),
	town VARCHAR(20),
	contactNo VARCHAR(15) NOT NULL,
	dateOfBirth DATETIME NOT NULL,
	gender VARCHAR(1) NOT NULL,
	PRIMARY KEY(cus_id) );
	
SELECT 'INSERTING DATA INTO TABLE CUSTOERS' as 'INFO';

INSERT INTO customers VALUES ( null, 'Treasa', 'Cummins', 'Cam', 'Curry', 'Brideswell', '0876534276', '1978-02-14', 'F');
INSERT INTO customers VALUES ( null, 'Donagh', 'Barry', 'Willow Park view',null, 'Athlone','0858945861', '1989-03-12', 'M');
INSERT INTO customers VALUES ( null, 'Finn', 'Dolan', 'Golf Course Rd',null, 'Moate', '0839012543', '1965-04-11', 'M');
INSERT INTO customers VALUES ( null, 'Ele', 'Carey', 'Knockraha','Glanmire', null, '0859870987', '1997-12-21', 'F');
INSERT INTO customers VALUES ( null, 'Denis', 'Fox', 'Lynn Rd','Lynn', 'Mullingar', '0877654321', '1976-01-19', 'M');

SELECT 'CHECKING TO SEE IF DATA INSERTED TO CUSTOMERS CORRECTLY' as 'INFO';

SELECT * FROM customers;

SELECT 'CREATING BOOKS TABLE' as 'INFO';

DROP TABLE IF EXISTS books;

CREATE TABLE books (
	book_id INTEGER AUTO_INCREMENT ,
	title VARCHAR(45) NOT NULL,
	author VARCHAR(25) NOT NULL,
	yearPublished VARCHAR(10) NOT NULL,
	quantity INTEGER NOT NULL,
	genre VARCHAR(30) NOT NULL,
	description VARCHAR(500),
	PRIMARY KEY(book_id) );
	
SELECT 'INSERTING DATA INTO TABLE BOOKS' as 'INFO';

INSERT INTO books VALUES ( null, 'To Kill a Mockingbird', 'Harper Lee', '1960-0-0', 23, 'Classic', 'The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it, To Kill A Mockingbird became both an instant bestseller and a critical success when it was first published in 1960.' );
INSERT INTO books VALUES ( null, 'Nineteen Eighty-Four', 'George Orwell', '1949-0-0', 12, 'Dystopian', 'Nineteen Eighty-Four (also published as 1984) is a dystopian social science fiction novel and cautionary tale by English writer George Orwell.' );
INSERT INTO books VALUES ( null, 'A Christmas Carol', 'Charles Dickens', '1843-0-0', 5, 'Fairy Tale', 'A Christmas Carol recounts the story of Ebenezer Scrooge, an elderly miser who is visited by the ghost of his former business partner Jacob Marley and the spirits of Christmas Past, Present and Yet to Come. After their visits, Scrooge is transformed into a kinder, gentler man.' );
INSERT INTO books VALUES ( null, 'Pride and Prejudice', 'Jane Austen', '1813-0-0', 7, 'Classic', 'The novel follows the character development of Elizabeth Bennet, the protagonist of the book, who learns about the repercussions of hasty judgments and comes to appreciate the difference between superficial goodness and actual goodness.' );
INSERT INTO books VALUES ( null, 'Ulysses', 'James Joyce', '1922-0-0', 10, 'Classicc', 'It is considered one of the most important works of modernist literature and has been called "a demonstration and summation of the entire movement."' );

SELECT 'CHECKING TO SEE IF DATA INSERTED TO BOOKS CORRECTLY' as 'INFO';

SELECT * FROM books;

SELECT 'CREATING RENTALS TABLE' as 'INFO';

DROP TABLE IF EXISTS rentals;

CREATE TABLE rentals (
	rental_id INTEGER AUTO_INCREMENT ,
	book_id INTEGER NOT NULL,
	cus_id INTEGER NOT NULL,
	emp_id INTEGER NOT NULL,
	dateRented DATETIME NOT NULL,
	returned BOOLEAN NOT NULL,
	PRIMARY KEY(rental_id),
	FOREIGN KEY (book_id) REFERENCES books (book_id),
	FOREIGN KEY (cus_id) REFERENCES customers (cus_id),
	FOREIGN KEY (emp_id) REFERENCES employees (emp_id));
	
SELECT 'INSERTING DATA INTO RENTALS PRODUCTS' as 'INFO';

INSERT INTO rentals VALUES (null, 1, 3, 1, '2022-09-15', TRUE);
INSERT INTO rentals VALUES (null, 1, 2, 1, '2022-09-16', TRUE);
INSERT INTO rentals VALUES (null, 3, 3, 1, '2022-09-16', TRUE);
INSERT INTO rentals VALUES (null, 4, 2, 1, '2022-09-17', FALSE);
INSERT INTO rentals VALUES (null, 5, 2, 1, '2022-09-17', TRUE);
INSERT INTO rentals VALUES (null, 1, 1, 1, '2022-09-18', TRUE);
INSERT INTO rentals VALUES (null, 1, 5, 2, '2022-09-19', TRUE);
INSERT INTO rentals VALUES (null, 3, 3, 2, '2022-09-20', FALSE);
INSERT INTO rentals VALUES (null, 1, 2, 2, '2022-09-21', TRUE);
INSERT INTO rentals VALUES (null, 5, 1, 2, '2022-09-22', TRUE);
INSERT INTO rentals VALUES (null, 1, 1, 2, '2022-09-23', TRUE);
INSERT INTO rentals VALUES (null, 2, 1, 3, '2022-09-24', TRUE);
INSERT INTO rentals VALUES (null, 3, 2, 4, '2022-09-24', TRUE);
INSERT INTO rentals VALUES (null, 4, 2, 3, '2022-09-25', FALSE);
INSERT INTO rentals VALUES (null, 5, 3, 3, '2022-09-27', TRUE);
INSERT INTO rentals VALUES (null, 1, 3, 4, '2022-09-27', TRUE);
INSERT INTO rentals VALUES (null, 2, 4, 3, '2022-09-29', TRUE);
INSERT INTO rentals VALUES (null, 1, 4, 4, '2022-09-29', TRUE);
INSERT INTO rentals VALUES (null, 1, 5, 5, '2022-09-30', TRUE);
INSERT INTO rentals VALUES (null, 2, 5, 5, '2022-09-30', TRUE);
INSERT INTO rentals VALUES (null, 2, 1, 1, '2022-09-30', TRUE);
INSERT INTO rentals VALUES (null, 5, 4, 4, '2022-10-01', FALSE);
INSERT INTO rentals VALUES (null, 3, 4, 5, '2022-10-01', TRUE);
INSERT INTO rentals VALUES (null, 5, 4, 2, '2022-10-01', TRUE);
INSERT INTO rentals VALUES (null, 5, 3, 2, '2022-10-02', TRUE);
INSERT INTO rentals VALUES (null, 1, 3, 1, '2022-10-02', FALSE);
INSERT INTO rentals VALUES (null, 2, 1, 1, '2022-10-03', TRUE);
INSERT INTO rentals VALUES (null, 3, 2, 3, '2022-10-03', TRUE);
INSERT INTO rentals VALUES (null, 4, 3, 1, '2022-10-03', TRUE);
INSERT INTO rentals VALUES (null, 5, 4, 3, '2022-10-04', FALSE);
INSERT INTO rentals VALUES (null, 3, 1, 2, '2022-10-04', TRUE);
INSERT INTO rentals VALUES (null, 4, 2, 4, '2022-10-04', TRUE);
INSERT INTO rentals VALUES (null, 5, 3, 5, '2022-10-05', FALSE);

SELECT 'CHECKING TO SEE IF DATA INSERTED TO RENTALS CORRECTLY' as 'INFO';

SELECT * FROM rentals;

/* cartesian Product - multiply 2 tables together */
select * from customers, employees;

/* union note: doesn't include duplicates */
(select firstName, lastName, town from customers) UNION (select firstName, lastName, town from employees);

/* inner join (intersection) */
/* goes through customer table and tries to match somethng in employees table */
select c.firstName, c.lastName, c.town
from customers as c inner join employees as e on
(c.firstName = e.firstName and c.lastName = e.lastName and c.town = e.town);
/* another way */
select c.firstName, c.lastName, c.town
from customers as c where EXISTS
(select e.firstName, e.lastName, e.town from employees as e
where c.firstName = e.firstName and c.lastName = e.lastName
and c.town = e.town);

/* except - gets everything in table one and not table 2 */
select c.firstName, c.lastName, c.town
from customers as c where not EXISTS
(select e.firstName, e.lastName, e.town from employees as e
where c.firstName = e.firstName and c.lastName = e.lastName
and c.town = e.town);

/* division - */
SELECT DISTINCT c1.y AS y FROM c c1
WHERE NOT EXISTS
(SELECT d.x FROM d WHERE d.x NOT IN 
(SELECT c2.x FROM c c2 WHERE c2.y = c1.y));

/* */
select rental_id, title, cus_id, emp_id, dateRented 
from rentals, books 
where rentals.book_id = books.book_id; /* column common between 2 tables is what we join them on */

/* dates */
select current_date();
select now();
select dayname(now()) as info;
select monthname(now()) as info;
select day(now()), month(now()), year(now());
select dayofmonth(now());
select dayofweek(now());
select dayofyear(now());
select dayofweek("2000-12-25"); /* gets day of the date */
/* add days */
select now(), date_add(now(), interval 4 day);
select now(), date_add(now(), interval 5 month);
select now(), date_add(now(), interval 6 year);
/* subtract days */
select now(), date_sub(now(), interval 4 day);
select now(), date_sub(now(), interval 5 month);
select now(), date_sub(now(), interval 6 year);
/* num of days between 2 dates */
select datediff(now(), "2023-11-01");
select datediff("2023-11-01", now());
select datediff(now(), "2022-09-01") as "Time in College";
/* get someones age */
/* datediff gets num of days*/
/* from_days gets a num of years from that */
/* formats as age */
select date_format(from_days(datediff(now(), "2003-08-11")), "%y") as age;

/* get random number */
select cast((rand() * 10) as unsigned integer);

/* Questions */
/* Oldest employee */
/*v1*/ select firstName, lastName, dateOfBirth from employees order by dateOfBirth limit 1;
/*v2*/ /* this way is better as it would return multiple results */ select firstName, lastName, dateOfBirth from employees where dateOfBirth = (select min(dateOfBirth) from employees);

/* ages of each employee */
select firstName, lastName, dateOfBirth,
date_format(from_days(datediff(now(), dateOfBirth)), "%y") as age from employees;
/* Ages of each customer */
select firstName, lastName, dateOfBirth,
date_format(from_days(datediff(now(), dateOfBirth)), "%y") as age from customers;
