-- ──────────────────────────────────────────────────
-- Problem  : 180. Consecutive Numbers
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/consecutive-numbers/
-- Runtime  : 546 ms (beats 88%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below
# Write your MySQL query statement below
with cte as (
    select num,
    lead(num,1) over() num1,
    lead(num,2) over() num2
    from logs

)

select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2)