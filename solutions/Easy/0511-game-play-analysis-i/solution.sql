-- ──────────────────────────────────────────────────
-- Problem  : 511. Game Play Analysis I
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/game-play-analysis-i/
-- Runtime  : 620 ms (beats 20%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select player_id,min(event_date) as first_login
from Activity
group by player_id