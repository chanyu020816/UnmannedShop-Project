## Create User Info Table
```bigquery
CREATE TABLE unmannedshop.User (
  user_id INT64,
  username STRING,
  email STRING,
  password STRING,
  Sex String,
  BirthDate DATE,
  registration_date DATE
);

INSERT INTO unmannedshop.User (user_id, username, email, password, Sex, BirthDate, registration_date) 
SELECT 0 AS user_id, 'Chanyu' AS username, 'trafalgarlaw0816@gmail.com' AS email,'chenyu910816' AS password,  
'Male' AS Sex, DATE('2002-08-16') AS BirthDate, DATE('2023-10-28') AS registration_date UNION ALL
SELECT 1 AS user_id, 'GilberStrang' AS username, 'gilbert@gmail.com' AS email,'gilbert01' AS password,  
'Male' AS Sex, DATE('1934-11-27') AS BirthDate, DATE('2023-10-28') AS registration_date UNION ALL
SELECT 2 AS user_id, 'Maokao' AS username, 'maokao@gmail.com' AS email,'maokao01' AS password,  
'Male' AS Sex, DATE('1980-03-15') AS BirthDate, DATE('2023-10-28') AS registration_date;
```

## Create Product Table

```bigquery
CREATE TABLE unmannedshop.Product (
  product_id INT64,
  product_name STRING,
  product_price INT64
);

ALTER TABLE unmannedshop.Product ADD PRIMARY KEY (product_id) NOT ENFORCED;

INSERT INTO unmannedshop.Product (product_id, product_name, product_price)
SELECT 0 AS product_id, 'Bak Kut Teh Flavor Noodles' AS product_name, 30 AS product_price UNION ALL
SELECT 1 AS product_id, 'Doritos' AS product_name, 30 AS product_price UNION ALL
SELECT 2 AS product_id, 'I MEI-Milk Puff' AS product_name, 40 AS product_price UNION ALL
SELECT 3 AS product_id, 'M-M-Crisp' AS product_name, 45 AS product_price UNION ALL
SELECT 4 AS product_id, 'M-M-Peanut' AS product_name, 45 AS product_price UNION ALL
SELECT 5 AS product_id, 'Oreo' AS product_name, 49 AS product_price UNION ALL
SELECT 6 AS product_id, 'Popconcern-Sweet-Salty' AS product_name, 65 AS product_price UNION ALL
SELECT 7 AS product_id, 'Pringles-Origin' AS product_name, 75 AS product_price UNION ALL
SELECT 8 AS product_id, 'PureTea-Black Tea' AS product_name, 25 AS product_price UNION ALL
SELECT 9 AS product_id, 'PureTea-LemonGreen Tea' AS product_name, 25 AS product_price UNION ALL
SELECT 10 AS product_id, 'Skittles' AS product_name, 39 AS product_price UNION ALL
SELECT 11 AS product_id, 'White Chocolate Ice Cream' AS product_name, 65 AS product_price
;

```

## Create Order History Table
```bigquery
CREATE TABLE unmannedshop.Order (
  order_id STRING,
  user_id INT64,
  machine_id INT64,
  order_date DATE,
  total_amount INT64
);
```

## Create Order Item Table
```bigquery
CREATE TABLE unmannedshop.OrderProduct (
  order_product_id STRING,
  order_id STRING,
  product_id INT64,
  number INT64
);

```
