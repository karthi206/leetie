-- ──────────────────────────────────────────────────
-- Problem  : 1075. Project Employees I
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/project-employees-i/
-- Runtime  : 496 ms (beats 92%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT p.project_id, ROUND(AVG(e.experience_years),2) AS average_years
FROM Project p 
LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id