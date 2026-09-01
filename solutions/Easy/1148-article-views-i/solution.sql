-- ──────────────────────────────────────────────────
-- Problem  : 1148. Article Views I
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/article-views-i/
-- Runtime  : 77 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select distinct author_id as id from Views
where author_id = viewer_id 
order by id;