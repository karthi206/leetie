-- ──────────────────────────────────────────────────
-- Problem  : 627. Swap Sex of Employees
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/swap-sex-of-employees/
-- Runtime  : 299 ms (beats 25%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

UPDATE salary SET sex =
CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;