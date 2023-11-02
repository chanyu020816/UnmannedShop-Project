## Create User Info Table
```bigquery
CREATE TABLE unmannedshop.TestUserInfoFull (
  user_id INT64,
  username STRING,
  email STRING,
  password STRING,
  Sex String,
  BirthDate DATE,
  registration_date DATE
);
INSERT INTO unmannedshop.TestUserInfoFull (user_id, username, email, password, Sex, BirthDate, registration_date) 
SELECT 0 AS user_id, 'Chanyu' AS username, 'trafalgarlaw0816@gmail.com' AS email,'chenyu910816' AS password,  
       'Male' AS Sex, DATE('2002-08-16') AS BirthDate, DATE('2023-10-28') AS registration_date;
```

## Create Item Table

```bigquery
CREATE TABLE unmannedshop.TestItemPrice (
  item_id INT64,
  item_name STRING,
  item_price INT64
);

INSERT INTO unmannedshop.TestItemPrice (item_id, item_name, item_price)
SELECT 0 AS item_id, 'Bak Kut Teh Flavor Noodles' AS item_name, 30 AS item_price UNION ALL
SELECT 1 AS item_id, 'Doritos' AS item_name, 30 AS item_price UNION ALL
SELECT 2 AS item_id, 'I MEI-Milk Puff' AS item_name, 40 AS item_price UNION ALL
SELECT 3 AS item_id, 'M-M-Crisp' AS item_name, 45 AS item_price UNION ALL
SELECT 4 AS item_id, 'M-M-Peanut' AS item_name, 45 AS item_price UNION ALL
SELECT 5 AS item_id, 'Oreo' AS item_name, 49 AS item_price UNION ALL
SELECT 6 AS item_id, 'Popconcern-Sweet-Salty' AS item_name, 65 AS item_price UNION ALL
SELECT 7 AS item_id, 'Pringles-Origin' AS item_name, 75 AS item_price UNION ALL
SELECT 8 AS item_id, 'PureTea-Black Tea' AS item_name, 25 AS item_price UNION ALL
SELECT 9 AS item_id, 'PureTea-LemonGreen Tea' AS item_name, 25 AS item_price UNION ALL
SELECT 10 AS item_id, 'Skittles' AS item_name, 39 AS item_price UNION ALL
SELECT 11 AS item_id, 'White Chocolate Ice Cream' AS item_name, 65 AS item_price
;

```

## Create Order History Table
```bigquery
CREATE TABLE unmannedshop.TestOrderHistory (
  order_id STRING,
  user_id INT64,
  order_date DATE,
  total_amount INT64
);
```

## Create Order Item Table
```bigquery
CREATE TABLE unmannedshop.TestOrderItems (
  order_item_id STRING,
  order_id STRING,
  item_id INT64,
  number INT64,
  item_price INT64
);

```
