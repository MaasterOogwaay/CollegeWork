/* count the number of employees in each department */
select department, count(*) as total
from details
group by department;

/* group by more than one column */
select department,position, count(*) as total
from details
group by department, position;

/* HAVING CLAUSE - find departments with more than x employees */
select department, count(*) as employees
from details
group by department
having count(*) > 3;

/* LIMIT CLAUSE - only shows value within the limit */
/* first 5 */
select * from details limit 5;

/* decending 1 */
select * from details order by id desc limit 5;

/* last 5 ascending */
select * from details limit 5 offset 15;

/* display employees older than average age */
select * from details where age > (select avg(age)
from details);

/* QUESTIONS */
/* details of employees not between ages 40 and 50 */
select * from details where age not between 40 and 50;

/* work between 10 and 15 hours per week */
select * from details where hours between 10 and 15;

/* all employees with an 'e' in their first name */
select * from details where firstName like "%e%";

/* all employees whose second letter of first name is 'u' */
select * from details where firstName like "_u%";

/* first name ends with 'n' and 4 letters in length */
select * from details where firstName like "%n" and length(firstName) = 4;
/* " " starts with 'J' and 4 letters in length */
select * from details where firstName like "J%" and length(firstName) = 4;
/* " " only 3 letters in length */
select * from details where firstName like "___";
/* " " greater than 4 letters in length */
select * from details where firstName like "_____%";

/* all female employees with '3' in their age */
select * from details where gender = "F" and age like "%3%";

/* count num of females */
select count(*) as noOfFemales from details where gender = "F";
/* count num of males */
select count(*) as noOfFemales from details where gender = "M";

/* average ages of females */
select avg(age) as femaleAvgAge from details where gender = "F";
/* average ages of males */
select avg(age) as maleAvgAge from details where gender = "M";

/* oldest employee */
select * from details order by age desc limit 1;

/* youngest employee */
select * from details order by age limit 1;

/* average hours */
select avg(hours) as avgHours from details;

/* sum of female wage */
select sum(rate*hours) from details where gender = "F";
/* sum of male wage */
select sum(rate*hours) from details where gender = "M";

/* avg age in each department */
select department, avg(age) from details group by department order by department;

/* avg age in each position */
select position, avg(age) from details group by position order by position;

/* avg age of each gender */
select gender, avg(age) from details group by gender order by gender;

/* number of males/females per department */
select department, gender, count(gender) as total from details group by gender, department order by department;

/* avg salary per department */
select department, avg(rate*hours) as avgWage from details group by department order by department;

/* average who earns more */
select gender, avg(rate*hours) as avgWage from details group by gender;

/* employees who earn more than avg wage in their apartment */
select *, (rate * hours) as wage
from details as d 
where (rate * hours) > 
    (select avg(rate*hours)
    from details as d2
    where d2.department = d.department);

