-- ──────────────────────────────────────────────────
-- Problem  : 1661. Average Time of Process per Machine
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/average-time-of-process-per-machine/
-- Runtime  : 271 ms (beats 55%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time 
from Activity a1
join Activity a2 
on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id