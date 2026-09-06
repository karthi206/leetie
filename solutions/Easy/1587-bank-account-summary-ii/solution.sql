-- ──────────────────────────────────────────────────
-- Problem  : 1587. Bank Account Summary II
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/bank-account-summary-ii/
-- Runtime  : 1075 ms (beats 21%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    u.name,
    SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t
    ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;