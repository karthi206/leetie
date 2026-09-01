-- ──────────────────────────────────────────────────
-- Problem  : 1211. Queries Quality and Percentage
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/queries-quality-and-percentage/
-- Runtime  : 3176 ms (beats 5%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from
queries
group by
query_name;