-- ──────────────────────────────────────────────────
-- Problem  : 1045. Customers Who Bought All Products
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/customers-who-bought-all-products/
-- Runtime  : 601 ms (beats 65%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT  customer_id FROM Customer GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)