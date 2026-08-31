-- ──────────────────────────────────────────────────
-- Problem  : 3436. Find Valid Emails
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/find-valid-emails/
-- Runtime  : 88 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT user_id, email
FROM Users
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+\\.com$'
ORDER BY user_id;