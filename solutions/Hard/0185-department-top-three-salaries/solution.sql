-- ──────────────────────────────────────────────────
-- Problem  : 185. Department Top Three Salaries
-- Difficulty: Hard
-- Tags     : Database
-- Link     : https://leetcode.com/problems/department-top-three-salaries/
-- Runtime  : 945 ms (beats 85%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below

WITH new_table AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY d.name
            ORDER BY e.salary DESC
        ) AS Ranking
    FROM Employee e
    LEFT JOIN Department d
        ON e.departmentId = d.id
)

SELECT
    Department,
    Employee,
    Salary
FROM new_table
WHERE Ranking <= 3;