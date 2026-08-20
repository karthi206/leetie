-- ──────────────────────────────────────────────────
-- Problem  : 577. Employee Bonus
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/employee-bonus/
-- Runtime  : 98 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empID = b.empID
WHERE b.bonus IS NULL OR b.bonus < 1000; 