-- ──────────────────────────────────────────────────
-- Problem  : 607. Sales Person
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/sales-person/
-- Runtime  : 1494 ms (beats 64%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below
select name 
from SalesPerson 
where sales_id Not in (select o.sales_id 
from Orders o
join company c
on o.com_id=c.com_id
where c.name ='Red')