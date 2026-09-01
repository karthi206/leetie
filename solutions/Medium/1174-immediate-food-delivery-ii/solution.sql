-- ──────────────────────────────────────────────────
-- Problem  : 1174. Immediate Food Delivery II
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/immediate-food-delivery-ii/
-- Runtime  : 85 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

Select round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);