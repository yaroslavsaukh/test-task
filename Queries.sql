--Query 1--
SELECT *
FROM `properties`
WHERE title LIKE "% quinta %" OR "% house %";

--Query 2--

SELECT *
FROM `properties`
WHERE features LIKE "% pool %"

--Query 3--

SELECT AVG(living_area)/AVG(price) AS Average
FROM `properties`
WHERE title LIKE "% Nagüeles %"

