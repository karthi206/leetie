-- ──────────────────────────────────────────────────
-- Problem  : 1341. Movie Rating
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/movie-rating/
-- Runtime  : 1454 ms (beats 57%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

(SELECT name AS results
FROM MovieRating JOIN Users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM MovieRating JOIN Movies USING(movie_id)
WHERE EXTRACT(YEAR_MONTH FROM created_at) = 202002
GROUP BY title
ORDER BY AVG(rating) DESC, title
LIMIT 1);