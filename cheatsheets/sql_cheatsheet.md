# 🗄️ SQL Quick Reference Cheatsheet

Essential SQL commands for database operations.

---

## 📊 Database Basics

### **Create & Drop Database**
```sql
-- Create database
CREATE DATABASE my_database;

-- Use database
USE my_database;

-- Drop database (CAREFUL!)
DROP DATABASE my_database;

-- Show databases
SHOW DATABASES;
```

---

## 📋 Table Operations

### **Create Table**
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- With foreign key
CREATE TABLE posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    title VARCHAR(200),
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### **Modify Table**
```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Drop column
ALTER TABLE users DROP COLUMN phone;

-- Modify column
ALTER TABLE users MODIFY COLUMN age SMALLINT;

-- Rename column
ALTER TABLE users RENAME COLUMN username TO user_name;

-- Rename table
RENAME TABLE users TO customers;
ALTER TABLE users RENAME TO customers;
```

### **Drop Table**
```sql
DROP TABLE users;
DROP TABLE IF EXISTS users;

-- Show tables
SHOW TABLES;

-- Describe table structure
DESCRIBE users;
DESC users;
```

---

## ➕ Insert Data
```sql
-- Insert single row
INSERT INTO users (username, email, age)
VALUES ('john_doe', 'john@example.com', 25);

-- Insert multiple rows
INSERT INTO users (username, email, age)
VALUES 
    ('jane_smith', 'jane@example.com', 30),
    ('bob_jones', 'bob@example.com', 28);

-- Insert from another table
INSERT INTO archived_users
SELECT * FROM users WHERE age > 65;
```

---

## 🔍 Select Data

### **Basic Select**
```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT username, email FROM users;

-- Select with alias
SELECT username AS name, email AS contact FROM users;

-- Select distinct values
SELECT DISTINCT age FROM users;

-- Limit results
SELECT * FROM users LIMIT 10;

-- Limit with offset
SELECT * FROM users LIMIT 10 OFFSET 20;
```

### **Where Clause**
```sql
-- Equal
SELECT * FROM users WHERE age = 25;

-- Not equal
SELECT * FROM users WHERE age != 25;
SELECT * FROM users WHERE age <> 25;

-- Comparison operators
SELECT * FROM users WHERE age > 18;
SELECT * FROM users WHERE age <= 30;

-- Between
SELECT * FROM users WHERE age BETWEEN 18 AND 30;

-- In list
SELECT * FROM users WHERE age IN (18, 21, 25);

-- Like (pattern matching)
SELECT * FROM users WHERE username LIKE 'john%';  -- Starts with john
SELECT * FROM users WHERE email LIKE '%@gmail.com';  -- Ends with @gmail.com
SELECT * FROM users WHERE username LIKE '%doe%';  -- Contains doe

-- IS NULL / IS NOT NULL
SELECT * FROM users WHERE phone IS NULL;
SELECT * FROM users WHERE phone IS NOT NULL;
```

### **Logical Operators**
```sql
-- AND
SELECT * FROM users WHERE age > 18 AND age < 30;

-- OR
SELECT * FROM users WHERE age < 18 OR age > 65;

-- NOT
SELECT * FROM users WHERE NOT age = 25;

-- Combining
SELECT * FROM users 
WHERE (age > 18 AND age < 30) OR username LIKE 'admin%';
```

---

## 🔄 Update Data
```sql
-- Update single column
UPDATE users SET age = 26 WHERE username = 'john_doe';

-- Update multiple columns
UPDATE users 
SET age = 26, email = 'newemail@example.com'
WHERE username = 'john_doe';

-- Update all rows (CAREFUL!)
UPDATE users SET active = 1;

-- Update with calculation
UPDATE products SET price = price * 1.1;
```

---

## ❌ Delete Data
```sql
-- Delete specific rows
DELETE FROM users WHERE age < 18;

-- Delete all rows (CAREFUL!)
DELETE FROM users;

-- Truncate (faster than DELETE, resets AUTO_INCREMENT)
TRUNCATE TABLE users;
```

---

## 📊 Sorting & Ordering
```sql
-- Sort ascending (default)
SELECT * FROM users ORDER BY age;
SELECT * FROM users ORDER BY age ASC;

-- Sort descending
SELECT * FROM users ORDER BY age DESC;

-- Multiple columns
SELECT * FROM users ORDER BY age DESC, username ASC;

-- Order by column number
SELECT username, age FROM users ORDER BY 2 DESC;
```

---

## 📈 Aggregate Functions
```sql
-- Count
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT age) FROM users;

-- Sum
SELECT SUM(price) FROM products;

-- Average
SELECT AVG(age) FROM users;

-- Min/Max
SELECT MIN(age) FROM users;
SELECT MAX(price) FROM products;

-- Multiple aggregates
SELECT 
    COUNT(*) AS total_users,
    AVG(age) AS avg_age,
    MIN(age) AS youngest,
    MAX(age) AS oldest
FROM users;
```

---

## 🔢 Group By
```sql
-- Basic grouping
SELECT age, COUNT(*) AS count
FROM users
GROUP BY age;

-- Multiple columns
SELECT city, state, COUNT(*) AS count
FROM users
GROUP BY city, state;

-- With HAVING (filter groups)
SELECT age, COUNT(*) AS count
FROM users
GROUP BY age
HAVING COUNT(*) > 5;

-- Group with WHERE and HAVING
SELECT city, AVG(age) AS avg_age
FROM users
WHERE age > 18
GROUP BY city
HAVING AVG(age) > 25
ORDER BY avg_age DESC;
```

---

## 🔗 Joins

### **Inner Join**
```sql
SELECT users.username, posts.title
FROM users
INNER JOIN posts ON users.id = posts.user_id;

-- Shorter alias
SELECT u.username, p.title
FROM users u
JOIN posts p ON u.id = p.user_id;
```

### **Left Join**
```sql
-- All users, even without posts
SELECT u.username, p.title
FROM users u
LEFT JOIN posts p ON u.id = p.user_id;
```

### **Right Join**
```sql
-- All posts, even without valid user
SELECT u.username, p.title
FROM users u
RIGHT JOIN posts p ON u.id = p.user_id;
```

### **Full Outer Join**
```sql
-- All users and all posts
SELECT u.username, p.title
FROM users u
FULL OUTER JOIN posts p ON u.id = p.user_id;

-- MySQL doesn't support FULL OUTER, use UNION
SELECT u.username, p.title
FROM users u LEFT JOIN posts p ON u.id = p.user_id
UNION
SELECT u.username, p.title
FROM users u RIGHT JOIN posts p ON u.id = p.user_id;
```

### **Self Join**
```sql
-- Find users in same city
SELECT u1.username, u2.username, u1.city
FROM users u1
JOIN users u2 ON u1.city = u2.city AND u1.id < u2.id;
```

### **Multiple Joins**
```sql
SELECT u.username, p.title, c.content
FROM users u
JOIN posts p ON u.id = p.user_id
JOIN comments c ON p.id = c.post_id;
```

---

## 🔎 Subqueries
```sql
-- Subquery in WHERE
SELECT username FROM users
WHERE age > (SELECT AVG(age) FROM users);

-- Subquery in FROM
SELECT avg_age_city FROM (
    SELECT city, AVG(age) AS avg_age
    FROM users
    GROUP BY city
) AS city_stats
WHERE avg_age > 25;

-- Subquery with IN
SELECT username FROM users
WHERE id IN (SELECT user_id FROM posts WHERE likes > 100);

-- EXISTS
SELECT username FROM users u
WHERE EXISTS (SELECT 1 FROM posts p WHERE p.user_id = u.id);
```

---

## 🔀 Set Operations
```sql
-- UNION (remove duplicates)
SELECT username FROM users
UNION
SELECT username FROM archived_users;

-- UNION ALL (keep duplicates)
SELECT username FROM users
UNION ALL
SELECT username FROM archived_users;

-- INTERSECT (common rows)
SELECT username FROM users
INTERSECT
SELECT username FROM premium_users;

-- EXCEPT (difference)
SELECT username FROM users
EXCEPT
SELECT username FROM banned_users;
```

---

## 🔢 String Functions
```sql
-- Concatenate
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;

-- Length
SELECT username, LENGTH(username) FROM users;

-- Uppercase/Lowercase
SELECT UPPER(username), LOWER(email) FROM users;

-- Substring
SELECT SUBSTRING(email, 1, 5) FROM users;

-- Replace
SELECT REPLACE(phone, '-', '') FROM users;

-- Trim
SELECT TRIM(username) FROM users;
```

---

## 📅 Date Functions
```sql
-- Current date/time
SELECT NOW();
SELECT CURRENT_DATE;
SELECT CURRENT_TIME;

-- Date parts
SELECT YEAR(created_at), MONTH(created_at), DAY(created_at) FROM users;

-- Date arithmetic
SELECT DATE_ADD(created_at, INTERVAL 7 DAY) FROM users;
SELECT DATE_SUB(NOW(), INTERVAL 1 MONTH);

-- Date difference
SELECT DATEDIFF(NOW(), created_at) AS days_since_created FROM users;

-- Format date
SELECT DATE_FORMAT(created_at, '%Y-%m-%d') FROM users;
SELECT DATE_FORMAT(created_at, '%M %d, %Y') FROM users;
```

---

## 🔐 Indexes
```sql
-- Create index
CREATE INDEX idx_username ON users(username);

-- Create unique index
CREATE UNIQUE INDEX idx_email ON users(email);

-- Composite index
CREATE INDEX idx_name ON users(first_name, last_name);

-- Drop index
DROP INDEX idx_username ON users;

-- Show indexes
SHOW INDEX FROM users;
```

---

## 🎯 Constraints
```sql
-- Primary key
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT
);

-- Foreign key
CREATE TABLE posts (
    id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Unique
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);

-- Not null
CREATE TABLE users (
    username VARCHAR(50) NOT NULL
);

-- Check (MySQL 8.0+)
CREATE TABLE users (
    age INT CHECK (age >= 18)
);

-- Default
CREATE TABLE users (
    status VARCHAR(20) DEFAULT 'active'
);
```

---

## 🔒 Transactions
```sql
-- Start transaction
START TRANSACTION;
BEGIN;

-- Make changes
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit (save changes)
COMMIT;

-- Rollback (undo changes)
ROLLBACK;

-- Savepoint
SAVEPOINT savepoint1;
ROLLBACK TO savepoint1;
```

---

## 👥 User Management
```sql
-- Create user
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
GRANT SELECT, INSERT ON database_name.* TO 'username'@'localhost';

-- Revoke privileges
REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'localhost';

-- Drop user
DROP USER 'username'@'localhost';

-- Show grants
SHOW GRANTS FOR 'username'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
```

---

## 💡 Common Patterns

### **Pagination**
```sql
-- Page 1 (items 1-10)
SELECT * FROM products LIMIT 10 OFFSET 0;

-- Page 2 (items 11-20)
SELECT * FROM products LIMIT 10 OFFSET 10;

-- Page N
SELECT * FROM products LIMIT 10 OFFSET (N-1)*10;
```

### **Find Duplicates**
```sql
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

### **Remove Duplicates**
```sql
DELETE u1 FROM users u1
INNER JOIN users u2
WHERE u1.id > u2.id AND u1.email = u2.email;
```

### **Top N per Group**
```sql
-- Top 3 products per category
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS rn
    FROM products
) AS ranked
WHERE rn <= 3;
```

### **Running Total**
```sql
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;
```

---

## 🎯 Best Practices

1. **Always use WHERE with UPDATE/DELETE** to avoid updating/deleting all rows
2. **Use transactions** for multiple related changes
3. **Create indexes** on columns used in WHERE, JOIN, ORDER BY
4. **Use EXPLAIN** to analyze query performance
5. **Normalize data** to reduce redundancy
6. **Use prepared statements** to prevent SQL injection
7. **Backup before major operations**

---

## 🔍 Performance Tips
```sql
-- Analyze query performance
EXPLAIN SELECT * FROM users WHERE age > 25;

-- Optimize table
OPTIMIZE TABLE users;

-- Analyze table
ANALYZE TABLE users;

-- Show slow queries (MySQL config)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;
```

---

## 📚 Resources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [SQLZoo](https://sqlzoo.net/) - Interactive tutorials

---

**Practice on sample databases to master SQL!**

*Updated: February 2026*