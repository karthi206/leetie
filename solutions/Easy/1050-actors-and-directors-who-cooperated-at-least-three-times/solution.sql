-- ──────────────────────────────────────────────────
-- Problem  : 1050. Actors and Directors Who Cooperated At Least Three Times
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
-- Runtime  : 373 ms (beats 77%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select actor_id, director_id 
from(
select actor_id,director_id, 
count(timestamp) as cooperated 
from ActorDirector 
group by actor_id,director_id) 
table1
where cooperated>=3;