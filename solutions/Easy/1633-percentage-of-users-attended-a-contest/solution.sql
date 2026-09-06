-- ──────────────────────────────────────────────────
-- Problem  : 1633. Percentage of Users Attended a Contest
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/percentage-of-users-attended-a-contest/
-- Runtime  : 122 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select 
contest_id, 
round(count(distinct user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
from  Register
group by contest_id
order by percentage desc,contest_id