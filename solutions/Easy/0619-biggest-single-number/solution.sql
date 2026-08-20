-- ──────────────────────────────────────────────────
-- Problem  : 619. Biggest Single Number
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/biggest-single-number/
-- Runtime  : 91 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_numbers;