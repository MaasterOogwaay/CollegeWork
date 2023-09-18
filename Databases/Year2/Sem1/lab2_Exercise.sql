Set up the sample database and answer the following questions:

How many tables are in the database? 
> 8

show tables from classicmodels;


Customer Table:
1.	How many customers are in the table?
> 122
select * from customers;
select count(*) from customers;

2.	List the different countries where the customers are from?
select country from customers;

3.	Write a query to list the Irish customers.
select * from customers where country = "Ireland";

4.	How many customers are from London?
select count(*) from customers where city = "London";

5.	Order the customers by creditLimit. What customer has the highest credit limit.
> (141) Diego Freyre
select * from customers order by creditLimit desc;

Employee Table:
1.	How many employees are there?
> 23
select count(*) from employees;
2.	Write a query to list the different job titles.
select distinct jobTitle from employees;
select jobTitle from employees;
3.	Find all employees whose firstName begins with ‘J’.
select * from employees where firstName like "J%";
4.	Find all employees whose firstName has 4 letters.
select * from employees where firstName like "____";
5.	Find all employees whose lastName begins with a ‘P’ and ends with an ‘n’.
select * from employees where lastName like "P%" and "%n";

Offices Table:
1.	Write a query to list the countries where offices are located.
select country from offices;
select distinct country from offices;

Products Table:
1.	Write a query to list all the product lines.
select productLine from products;
select distinct productLine from products;
2.	Order the data by buyPrice. What is the most expensive product?
> s10_4962 buyPrice = 103.42
select * from products order by buyPrice desc;
3.	List all the products that have the word ‘ford’ in the productName.
select * from products where productName like "%ford%";
