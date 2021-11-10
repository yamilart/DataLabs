# Select all the actors with the first name ‘Scarlett’.
select * from actor where first_name = "Scarlett";

# How many films (movies) are available for rent and how many films have been rented?
select count(film_id) as films_available from film;
select count(rental_id) as films_rented from rental;

# What are the shortest and longest movie duration? Name the values max_duration and min_duration.
select min(length) as min_duration, max(length) as max_duration 
from film;

# What's the average movie duration expressed in format (hours, minutes)?
select substring_index(sec_to_time(avg(length)*60), ":", 2) 
as average_duration from film;

# How many distinct (different) actors' last names are there?
select count(distinct(last_name)) as unique_last_names from actor;

# Since how many days has the company been operating (check DATEDIFF() function)?
select datediff(max(rental_date), min(rental_date)) as days_open from rental;

# Show rental info with additional columns month and weekday. Get 20 results.
select *, date_format(convert(rental_date, date),"%M") as rental_month,
date_format(convert(rental_date, date),"%W") as rental_day
from rental limit 20;

# Add an additional column day_type with values 'weekend' and 'workday' depending on the rental day of the week.
select *,
case
when date_format(convert(rental_date, date),"%w") = 5 then "weekend"
when date_format(convert(rental_date, date),"%w") = 6 then "weekend"
else "workday"
end
as weekend_or_weekday from rental
end;
# How many rentals were in the last month of activity?
select max(rental_date) from rental;
select count(rental_date) as last_month_rentals from rental
where rental_date like '2006-02%';