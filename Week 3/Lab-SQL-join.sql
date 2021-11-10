# List number of films per category.
select c.name, count(f.film_id) as amount
from category c 
join film_category f
on f.category_id = c.category_id
group by c.category_id, c.name;


# Display the first and last names, as well as the address, of each staff member.
select s.first_name, s.last_name, a.address
from staff s
join address a
on s.address_id = a.address_id;


# Display the total amount rung up by each staff member in August of 2005.
select s.first_name, s.last_name, sum(p.amount) as total_rung
from staff s
join payment p
on s.staff_id = p.staff_id
where p.payment_date like '2005-08%'
group by s.first_name, s.last_name;


# List each film and the number of actors who are listed for that film.
select f.title, count(fa.actor_id) as no_actors
from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id
group by f.title;


# Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name.
select c.first_name, c.last_name, sum(p.amount) as total_paid
from payment p
join customer c
on c.customer_id = p.customer_id
group by first_name, last_name
order by last_name;
