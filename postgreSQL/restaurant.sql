CREATE TABLE restaurant (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR,
    distance INTEGER,
    stars INTEGER CHECK (stars <= 5),
    category VARCHAR,
    favdish VARCHAR,
    takeout BOOLEAN,
    lastvisit DATE
)

INSERT INTO restaurant VALUES (
  DEFAULT, 'Gugliani', 4, 3, 'Italian', 'Fettucine Alfredo', TRUE, '2018-03-21'
)

INSERT INTO restaurant VALUES (
  DEFAULT, 'El Ranchero', 3, 4, 'Mexican', 'Fajitas', TRUE, '2018-02-21'
)

INSERT INTO restaurant VALUES (
  DEFAULT, 'Calliopes', 2, 2, 'Seafood', 'Shrimp Poboy', TRUE, '2018-03-14'
)

UPDATE restaurant SET takeout = FALSE WHERE name = 'El Ranchero';

INSERT INTO restaurant VALUES (
  DEFAULT, 'Chuys', 14, 5, 'Mexican', 'Fajitas', FALSE, '2017-12-14'
)

INSERT INTO restaurant VALUES (
  DEFAULT, 'Old Hickory Inn', 3, 4, 'Bar B Que', 'Gyros', TRUE, '2018-01-10'
)

-- QUERIES
SELECT * FROM restaurant WHERE stars = 5;
SELECT favdish FROM restaurant;
SELECT ID FROM restaurant WHERE name = 'El Ranchero';
SELECT * FROM restaurant WHERE category = 'Mexican';
SELECT * FROM restaurant WHERE takeout = TRUE;
SELECT * FROM restaurant WHERE takeout = TRUE AND category = 'Bar B Que';
SELECT * FROM restaurant WHERE distance <= 3;
SELECT * FROM restaurant WHERE lastvisit < '2018-04-01';
SELECT * FROM restaurant WHERE lastvisit < '2018-03-01' and stars = 5;

-- AGGREGATION QUERIES
SELECT * FROM restaurant ORDER BY distance;
SELECT * FROM restaurant ORDER BY distance LIMIT 2;
SELECT * FROM restaurant ORDER BY stars DESC LIMIT 2;
SELECT * from restaurant WHERE distance <= 2 ORDER BY stars DESC LIMIT 2;
SELECT COUNT(*) FROM restaurant;
SELECT COUNT(category) FROM restaurant GROUP BY category;
SELECT category, AVG(stars) FROM restaurant GROUP BY category;
SELECT category, MAX(stars) FROM restaurant GROUP BY category;