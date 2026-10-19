-- Write your query below
SELECT first_name, last_name, city, state
FROM person as p
LEFT JOIN address as a
ON p.person_id = a.person_id