-- ──────────────────────────────────────────────────
-- Problem  : 178. Rank Scores
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/rank-scores/
-- Runtime  : 64 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT S.score ,COUNT(S2.SCORE) as `rank` FROM SCORES S,
(SELECT DISTINCT SCORE FROM SCORES)  S2
WHERE S.SCORE<=S2.SCORE 
GROUP BY S.ID 
ORDER BY S.SCORE DESC;