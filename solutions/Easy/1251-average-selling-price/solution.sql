-- ──────────────────────────────────────────────────
-- Problem  : 1251. Average Selling Price
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/average-selling-price/
-- Runtime  : 794 ms (beats 86%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id