-- ──────────────────────────────────────────────────
-- Problem  : 602. Friend Requests II: Who Has the Most Friends
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Runtime  : 69 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────


with base as(select requester_id id from RequestAccepted
union all
select accepter_id id from RequestAccepted)


select id, count(*) num  from base group by 1 order by 2 desc limit 1