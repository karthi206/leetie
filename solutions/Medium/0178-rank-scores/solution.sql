-- ──────────────────────────────────────────────────
-- Problem  : 178. Rank Scores
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/rank-scores/
-- Runtime  : 395 ms (beats 29%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT S.score ,COUNT(S2.SCORE) as `rank` FROM SCORES S,
(SELECT DISTINCT SCORE FROM SCORES)  S2
WHERE S.SCORE<=S2.SCORE 
GROUP BY S.ID 
ORDER BY S.SCORE DESC;