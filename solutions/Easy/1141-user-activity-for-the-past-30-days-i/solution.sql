-- ──────────────────────────────────────────────────
-- Problem  : 1141. User Activity for the Past 30 Days I
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- Runtime  : 485 ms (beats 85%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT 
    a.activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM activity a
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date;