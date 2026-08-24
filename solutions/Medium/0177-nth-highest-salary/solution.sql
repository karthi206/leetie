-- ──────────────────────────────────────────────────
-- Problem  : 177. Nth Highest Salary
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/nth-highest-salary/
-- Runtime  : 93 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    SELECT salary FROM
        (SELECT 
        salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
        FROM Employee) AS t
    WHERE rnk = N
    LIMIT 1
  );
END