# Explore tables
select * from film;
select * from language;
# Select one column from a table. Get film titles.
select title from film;
# Select one column from a table and alias it. Get unique list of film languages under the alias language.
select distinct name as language from language;
# How many stores does the company have?
select count(distinct store_id) from store;
# How many employees staff does the company have?
select count(distinct staff_id) from staff;
# Return a list of employee first names only
select first_name from staff;