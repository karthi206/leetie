-- ──────────────────────────────────────────────────
-- Problem  : 1158. Market Analysis I
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/market-analysis-i/
-- Runtime  : 155 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id
    AND o.order_date >= '2019-01-01'
    AND o.order_date < '2020-01-01'
GROUP BY
    u.user_id,
    u.join_date;