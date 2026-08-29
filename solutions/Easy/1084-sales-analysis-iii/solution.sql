-- ──────────────────────────────────────────────────
-- Problem  : 1084. Sales Analysis III
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/sales-analysis-iii/
-- Runtime  : 108 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT p.product_id ,p.product_name
FROM product p
JOIN sales s
    ON p.product_id=s.product_id
GROUP BY p.product_id,p.product_name
HAVING MIN(s.sale_date)>= '2019-01-01'
    AND MAX(s.sale_date)<= '2019-03-31'