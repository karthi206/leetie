-- ──────────────────────────────────────────────────
-- Problem  : 610. Triangle Judgement
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/triangle-judgement/
-- Runtime  : 346 ms (beats 28%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below
select *, if(x+y>z and y+z>x and x+z>y, "Yes","No") as triangle from triangle