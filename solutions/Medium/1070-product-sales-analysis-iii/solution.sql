-- ──────────────────────────────────────────────────
-- Problem  : 1070. Product Sales Analysis III
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/product-sales-analysis-iii/
-- Runtime  : 68 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select product_id, min(year) as first_year, quantity, price 
from sales
group by product_id