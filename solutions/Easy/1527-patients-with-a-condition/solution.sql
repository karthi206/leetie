-- ──────────────────────────────────────────────────
-- Problem  : 1527. Patients With a Condition
-- Difficulty: Easy
-- Tags     : Database
-- Link     : https://leetcode.com/problems/patients-with-a-condition/
-- Runtime  : 432 ms (beats 64%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'