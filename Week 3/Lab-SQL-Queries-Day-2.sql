# Get release years.
select distinct release_year from film;


# Get all films with ARMAGEDDON in the title.
select * from film where title LIKE "%armageddon%";


# Get all films which title ends with APOLLO.
select * from film where title LIKE "%apollo";


# Get the 10 longest films.
select * from film
order by length DESC
limit 10;


# How many films include Behind the Scenes content?
select count(*) from film
where special_features LIKE "%behind the scenes%";


# Drop column picture from staff.
alter table staff
drop column picture;


# A new person is hired to help Jon. Her name is TAMMY SANDERS, and she is a customer. Update the database accordingly.
select * from staff; #checking the staff table
select * from customer
where first_name = 'tammy'; #checking the info for Tammy
insert into staff
values
('3',
'TAMMY',
'SANDERS',
'79',
'TAMMY.SANDERS@sakilacustomer.org',
'2',
'1',
'Tammy',
'',
CURRENT_TIMESTAMP);
select * from staff; #checking the info


# Add rental for movie "Academy Dinosaur" by Charlotte Hunter from Mike Hillyer at Store 1.
#You can use current date for the rental_date column in the rental table. and use similar method to get inventory_id, film_id, and staff_id.
select max(rental_id) from rental; #checking the last rental id number
select * from film
where title like "%dinosaur%"; #checking the info about the dinosaur movie
select * from inventory
where film_id = 1; #checking the inventory id number
select customer_id from sakila.customer
where first_name = 'CHARLOTTE' and last_name = 'HUNTER'; #checking customer id
insert into rental
values
(16050,
CURRENT_TIMESTAMP,
1,
130,
NULL,
'1',
CURRENT_TIMESTAMP);
select * from rental
where rental_id = 16050; #checking info


# Delete non-active users, but first, create a backup table deleted_users to store customer_id, email, 
#and the date for the users that would be deleted. Follow these steps:
#Check if there are any non-active users
SELECT * from customer
where active = 0;

#Create a table backup table as suggested
create table deleted_users LIKE customer;

#Insert the non active users in the table backup table
insert into deleted_users
select * 
from customer
where active = 0;

#Delete the non active users from the table customer
delete from customer 
where active = 0;