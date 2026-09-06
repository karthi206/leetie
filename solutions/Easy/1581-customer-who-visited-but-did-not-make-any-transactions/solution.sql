-- ──────────────────────────────────────────────────
-- Problem  : 1581. Customer Who Visited but Did Not Make Any Transactions
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
-- Runtime  : 1612 ms (beats 39%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────


SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans 
from Visits v 
LEFT JOIN Transactions t 
ON v.visit_id = t.visit_id  
WHERE t.transaction_id IS NULL 
GROUP BY v.customer_id; 
