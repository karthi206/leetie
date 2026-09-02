-- ──────────────────────────────────────────────────
-- Problem  : 1204. Last Person to Fit in the Bus
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/last-person-to-fit-in-the-bus/
-- Runtime  : 1736 ms (beats 17%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1