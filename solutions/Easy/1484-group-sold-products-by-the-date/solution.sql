-- ──────────────────────────────────────────────────
-- Problem  : 1484. Group Sold Products By The Date
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/group-sold-products-by-the-date/
-- Runtime  : 458 ms (beats 78%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select sell_date, count( DISTINCT product ) as num_sold ,
    
    GROUP_CONCAT( DISTINCT product order by product ASC separator ',' ) as products
    
        FROM Activities GROUP BY sell_date order by sell_date ASC;