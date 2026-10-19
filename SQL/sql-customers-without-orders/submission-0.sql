SELECT name
FROM customers
WHERE customers.name NOT IN (
    SELECT name
    FROM customers
    JOIN orders ON
    customers.id = orders.customer_id
)