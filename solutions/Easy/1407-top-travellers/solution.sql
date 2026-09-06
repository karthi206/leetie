-- ──────────────────────────────────────────────────
-- Problem  : 1407. Top Travellers
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/top-travellers/
-- Runtime  : 885 ms (beats 69%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT DISTINCT
    u.name,
    IFNULL(
        SUM(t.distance) OVER (PARTITION BY u.id),
        0
    ) AS travelled_distance
FROM Users u
LEFT JOIN Rides t
    ON u.id = t.user_id
ORDER BY travelled_distance DESC, u.name ASC;