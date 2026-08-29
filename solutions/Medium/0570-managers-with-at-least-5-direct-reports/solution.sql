-- ──────────────────────────────────────────────────
-- Problem  : 570. Managers with at Least 5 Direct Reports
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Runtime  : 65 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below
Select m.name
from employee as e
inner join employee as m
on e.managerId=m.id
group by e.managerId 
having count(e.id)>=5