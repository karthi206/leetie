-- ──────────────────────────────────────────────────
-- Problem  : 1068. Product Sales Analysis I
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/product-sales-analysis-i/
-- Runtime  : 97 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT product_name, year, price 
FROM Sales S 
INNER JOIN Product P 
ON S.product_id = P.product_id;