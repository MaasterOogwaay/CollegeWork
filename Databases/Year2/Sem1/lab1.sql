/* create table */
create table my_info(
    id integer not null,
    first_name char(12),
    last_name char(20),
    gender char(1)
);

create table details(
    id integer auto_increment not null primary key,
    firstName varchar(15) not null,
    lastName varchar(20) not null,
    age integer not null,
    gender varchar(1) not null,
    position varchar(15) not null,
    department varchar(20) not null,
    rate decimal(7, 2) not null,
    hours integer not null,
)