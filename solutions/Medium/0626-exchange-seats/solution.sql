-- ──────────────────────────────────────────────────
-- Problem  : 626. Exchange Seats
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/exchange-seats/
-- Runtime  : 68 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select case when id % 2 =1 and id+1 in (select id from Seat) then id+1
            when id % 2 =0 then id-1
            else id
        end as id, student
        from Seat
        order by id;