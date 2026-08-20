-- ──────────────────────────────────────────────────
-- Problem  : 584. Find Customer Referee
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/find-customer-referee/
-- Runtime  : 62 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below
select name from customer where referee_id != 2 or referee_id is null;