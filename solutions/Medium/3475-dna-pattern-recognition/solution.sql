-- ──────────────────────────────────────────────────
-- Problem  : 3475. DNA Pattern Recognition 
-- Difficulty: Medium
-- Tags     : Database
-- Link     : https://leetcode.com/problems/dna-pattern-recognition/
-- Runtime  : 100 ms (beats 0%)
-- Memory   : 0B (beats 0%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

# Write your MySQL query statement below
select  sample_id, dna_sequence, species, 
   (case when dna_sequence like "ATG%" then 1  else 0 end) as has_start,
   (case when regexp_like (dna_sequence,"TAA$|TAG$|TGA$") then 1 else 0 end) as has_stop,
   (case when dna_sequence like "%ATAT%" then 1 else 0 end) as has_atat,
   (case when dna_sequence like "%GGG%" then 1 else 0 end) as has_ggg
from Samples
group by sample_id;
