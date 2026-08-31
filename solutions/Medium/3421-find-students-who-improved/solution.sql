-- ──────────────────────────────────────────────────
-- Problem  : 3421. Find Students Who Improved
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/find-students-who-improved/
-- Runtime  : 309 ms (beats 71%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

WITH Ranked AS (
    SELECT
    student_id,
    subject,
    FIRST_VALUE(score) OVER(PARTITION BY student_id,subject ORDER BY exam_date) AS first_score,
    FIRST_VALUE(score) OVER(PARTITION BY student_id,subject ORDER BY exam_date DESC) AS latest_score
    FROM Scores
)
SELECT DISTINCT * FROM Ranked
WHERE first_score<latest_score
ORDER BY student_id,subject