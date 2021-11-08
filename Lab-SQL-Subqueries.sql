# How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT 
    COUNT(i.inventory_id) AS copies_in_inventory,
    f.title AS title
FROM
    inventory i
        JOIN
    film f USING (film_id)
WHERE
    i.film_id IN (SELECT 
            film_id
        FROM
            film
        WHERE
            title = 'Hunchback Impossible')
GROUP BY i.film_id;


# List all films whose length is longer than the average of all the films.
SELECT 
    film_id, title, length
FROM
    film
HAVING length > (SELECT 
        FLOOR(AVG(length))
    FROM
        film)
ORDER BY length DESC;


# Use subqueries to display all actors who appear in the film Alone Trip.
-- With title subquerying wouldn't be necessary --
SELECT 
    a.actor_id, a.first_name, a.last_name, f.title
FROM
    actor a
        JOIN
    film_actor fa USING (actor_id)
        JOIN
    film f USING (film_id)
WHERE
    fa.film_id = (SELECT 
            film_id
        FROM
            film
        WHERE
            title = 'Alone Trip')
GROUP BY a.actor_id , f.title;
-- Without Title --
SELECT 
    a.actor_id, a.first_name, a.last_name
FROM
    actor a
        JOIN
    film_actor fa USING (actor_id)
WHERE
    fa.film_id = (SELECT 
            film_id
        FROM
            film
        WHERE
            title = 'Alone Trip')
GROUP BY a.actor_id;


# Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
# Identify all movies categorized as family films.
SELECT 
    f.film_id, f.title, c.name
FROM
    film f
        JOIN
    film_category fc USING (film_id)
        JOIN
    category c USING (category_id)
WHERE
    fc.category_id IN (SELECT 
            category_id
        FROM
            category
        WHERE
            name = 'Family')
ORDER BY f.film_id;


# Get name and email from customers from Canada using subqueries. Do the same with joins. 
# Note that to create a join, you will have to identify the correct tables with their primary keys and foreign keys, that will help you get the relevant information.
-- Subqueries --
SELECT 
    c.first_name, c.email
FROM
    customer c
        JOIN
    address a USING (address_id)
        JOIN
    city ci USING (city_id)
WHERE
    ci.country_id = (SELECT 
            country_id
        FROM
            country
        WHERE
            country = 'Canada');
-- Joins -- 
SELECT 
    c.first_name, c.email, co.country
FROM
    customer c
        JOIN
    address a USING (address_id)
        JOIN
    city ci USING (city_id)
        JOIN
    country co USING (country_id)
WHERE
    co.country = 'Canada';


# Which are films starred by the most prolific actor? 
# Most prolific actor is defined as the actor that has acted in the most number of films. 
# First you will have to find the most prolific actor and then use that actor_id to find the different films that he/she starred.
SELECT 
    f.title, a.first_name, a.last_name
FROM
    film f
        JOIN
    film_actor fa USING (film_id)
        JOIN
    actor a USING (actor_id)
WHERE
    fa.actor_id = (SELECT 
            fa.actor_id
        FROM
            film_actor fa
        GROUP BY fa.actor_id
        ORDER BY COUNT(fa.actor_id) DESC
        LIMIT 1);


# Films rented by most profitable customer. 
# You can use the customer table and payment table to find the most profitable customer ie the customer that has made the largest sum of payments
SELECT DISTINCT
    f.title as films_rented_by_most_profitable_customer
FROM
    film f
        JOIN
    inventory i USING (film_id)
        JOIN
    rental r USING (inventory_id)
        JOIN
    payment p USING (customer_id)
WHERE
    p.customer_id = (SELECT 
            p.customer_id
        FROM
            payment p
        GROUP BY p.customer_id
        ORDER BY SUM(p.payment_id) DESC
        LIMIT 1);

# Customers who spent more than the average payments.
SELECT 
    last_name, first_name
FROM
    customer
WHERE
    customer_id IN (SELECT DISTINCT
            customer_id
        FROM
            payment
        WHERE
            amount > (SELECT 
                    AVG(amount)
                FROM
                    payment));