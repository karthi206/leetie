-- ──────────────────────────────────────────────────
-- Problem  : 1327. List the Products Ordered in a Period
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/list-the-products-ordered-in-a-period/
-- Runtime  : 784 ms (beats 62%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

Select p.product_name, Sum(o.unit) as unit from
Orders o Left Join Products p
on o.product_id = p.product_id
where o.order_date between '2020-02-01' and '2020-02-29'
group by p.product_name
having Sum(o.unit) >= 100