-- ──────────────────────────────────────────────────
-- Problem  : 1393. Capital Gain/Loss
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/capital-gainloss/
-- Runtime  : 543 ms (beats 64%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT stock_name,
    SUM(CASE WHEN operation = 'Buy' THEN -price ELSE +price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name
ORDER BY capital_gain_loss;