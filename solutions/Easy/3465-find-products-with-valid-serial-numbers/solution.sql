-- ──────────────────────────────────────────────────
-- Problem  : 3465. Find Products with Valid Serial Numbers
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/find-products-with-valid-serial-numbers/
-- Runtime  : 92 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT
    product_id,
    product_name,
    description
FROM products
WHERE REGEXP_LIKE(
    description COLLATE utf8mb3_bin,
    '(^|[^A-Za-z0-9])SN[0-9]{4}-[0-9]{4}([^A-Za-z0-9]|$)'
)
ORDER BY product_id;