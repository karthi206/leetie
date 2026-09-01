-- ──────────────────────────────────────────────────
-- Problem  : 1164. Product Price at a Given Date
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/product-price-at-a-given-date/
-- Runtime  : 680 ms (beats 28%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    p.product_id
    ,COALESCE((
        SELECT pr.new_price
        FROM products pr
        WHERE p.product_id=pr.product_id
            AND pr.change_date<='2019-08-16'
        ORDER BY pr.change_date DESC LIMIT 1
    ),10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM products 
) AS p