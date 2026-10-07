-- CREATE TABLE customers(
-- customer_id INT PRIMARY KEY,
-- name VARCHAR(100) NOT NULL,
-- city VARCHAR(100));

-- SELECT * FROM customers;

-- CREATE TABLE orders(
-- order_id INT PRIMARY KEY,
-- customer_id INT REFERENCES customers(customer_id),
-- amount INTEGER,
-- status VARCHAR(50)
-- );

SELECT * from orders;
-- INSERT INTO customers(customer_id,name,city) VALUES
-- (1,'Aman','Mumbai'),
-- (2,'Priya','Delhi'),
-- (3,'Rahul','Mumbai'),
-- (4,'Sneha','Pune'),
-- (5,'Vikram','Delhi'),
-- (6,'Neha','Kolkata');

-- INSERT INTO orders(order_id,customer_id,amount,status) VALUES
-- (101,1,500,'DELIVERED'),
-- (102,2,1200,'DELIVERED'),
-- (103,1,800,'CANCELLED'),
-- (104,3,1500,'DELIVERED'),
-- (105,2,450,NULL),
-- (106,5,2000,'DELIVERED'),
-- (107,4,700,'CANCELLED'),
-- (108,3,850,'DELIVERED');

-- using customers and orders each city and its total order amount but only cities whose total is more than 1000. Sort by total,highestfirst
--tHE SQL quesry is:
SELECT c.city, SUM(o.amount) AS total_order_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING SUM(o.amount) > 1000
ORDER BY total_order_amount DESC;

SELECT COUNT(status) FROM orders; -- 7