-- ──────────────────────────────────────────────────
-- Problem  : 1148. Article Views I
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/article-views-i/
-- Runtime  : 453 ms (beats 55%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select distinct author_id as id from Views
where author_id = viewer_id 
order by id;