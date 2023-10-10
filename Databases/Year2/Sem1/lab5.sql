/* Q1 - Name of the most rented book */
/* v1 */
select books.book_id, title, count(*) as total
from books, rentals
where books.book_id = rentals.book_id
group by books.book_id
order by total desc limit 1;

/* v2 */
select books.book_id, title, count(*) as total
from books inner join rentals on
(books.book_id = rentals.book_id)
group by books.book_id
order by total desc limit 1;

/* Q2 - Who is the best customer */
select customers.cus_id, firstName, lastName, count(*) as total
from customers inner join rentals on
(customers.cus_id = rentals.cus_id)
group by customers.cus_id
order by total desc limit 1;

/* Q3 - List top rental by genre */
select books.book_id, title, genre, count(*) as total
from books inner join rentals on
(books.book_id = rentals.book_id)
group by books.book_id
order by books.book_id;

update books set genre = "Classic" where book_id = 5;

(select books.book_id, title, genre, count(*) as total
from books inner join rentals on
(books.book_id = rentals.book_id)
where genre = "Classic"
group by books.book_id
order by total desc limit 1)
union
(select books.book_id, title, genre, count(*) as total
from books inner join rentals on
(books.book_id = rentals.book_id)
where genre = "Dystopian"
group by books.book_id
order by total desc limit 1)
union
(select books.book_id, title, genre, count(*) as total
from books inner join rentals on
(books.book_id = rentals.book_id)
where genre = "Fairy Tale"
group by books.book_id
order by total desc limit 1);

/* WHo is the best employee */
select employees.emp_id, firstName, lastName, count(*) as total
from employees inner join rentals on
(employees.emp_id = rentals.emp_id)
group by employees.emp_id
order by total desc limit 1;

/* Which book was rented out first */
select title, dateRented
from books inner join rentals on
(books.book_id = rentals.book_id)
where dateRented = (select min(dateRented) from rentals);

/* Which book was rented out last */
select title, dateRented
from books inner join rentals on
(books.book_id = rentals.book_id)
where dateRented = (select max(dateRented) from rentals);

/* Which book was never rented out */
insert into books values(null, "Dracula", "Bram Stoker", "1897-0-0", 4, "Horror", "Vampire Story!");

select c.title
from books as c where not EXISTS
(select e.book_id from rentals as e
where c.book_id = e.book_id);

/* Top 3 rentals for September 2022 */
select books.book_id, title, count(*) as total
from books inner join rentals on
(books.book_id = rentals.book_id)
where month(dateRented) = "9" and year(dateRented) = "2022"
group by books.book_id
order by total desc limit 3;

/* Top 3 rentals for October 2022 */
select books.book_id, title, count(*) as total
from books inner join rentals on
(books.book_id = rentals.book_id)
where month(dateRented) = "10" and year(dateRented) = "2022"
group by books.book_id
order by total desc limit 3;

/* Reproduce Rentals table with meaningful data */
select rental_id, title, customers.firstName as cFirstName, customers.lastName as cLastName, employees.firstName as eFirstName, employees.lastName as eLastName, dateRented 
from rentals, books, customers, employees
where rentals.book_id = books.book_id;

select rental_id, employees.firstName as eFirstName, employees.lastName as eLastName, customers.firstName as cFirstName, customers.lastName as cLastName, dateRented
from rentals, employees, customers, books
where rentals.emp_id = employees.emp_id
    and rentals.cus_id = customers.cus_id
    and rentals.book_id = books.book_id;
