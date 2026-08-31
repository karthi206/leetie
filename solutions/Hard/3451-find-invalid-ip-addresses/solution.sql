-- ──────────────────────────────────────────────────
-- Problem  : 3451. Find Invalid IP Addresses
-- Difficulty: Hard
-- Tags     : Database
-- Link     : https://leetcode.com/problems/find-invalid-ip-addresses/
-- Runtime  : 330 ms (beats 23%)
-- Memory   : 0B (beats 100%)
-- Language : mysql
-- Copyright: (c) 2026 karthi206. All rights reserved.
-- Synced by: leetie
-- ──────────────────────────────────────────────────

WITH ipseparated AS (
    SELECT
        ip,
        CASE
            WHEN CAST(SUBSTRING_INDEX(ip, '.', 1) AS UNSIGNED) > 255
            THEN 'invalid'
            ELSE 'valid'
        END AS part1,
        CASE
            WHEN LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1)) > 1
                 AND SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1)
                     REGEXP '^0[0-9]+'

                or CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS UNSIGNED) > 255
            THEN 'invalid'
            ELSE 'valid'
        END AS part2,
            CASE
            WHEN LENGTH(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1)) > 1
                 AND SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1)
                     REGEXP '^0[0-9]+'

                or CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS UNSIGNED) > 255
            THEN 'invalid'
            ELSE 'valid'
        END AS part3,

            CASE
            WHEN LENGTH(SUBSTRING_INDEX(ip, '.', -1)) > 1
                 AND SUBSTRING_INDEX(ip, '.', -1)
                     REGEXP '^0[0-9]+'

                or CAST(SUBSTRING_INDEX(ip, '.', -1) AS UNSIGNED) > 255
            THEN 'invalid'
            ELSE 'valid'
        END AS part4,
        COUNT(*) AS invalid_count
    FROM logs
    GROUP BY ip

)
select  ip , invalid_count 
from ipseparated
where 
(LENGTH(ip) - LENGTH(REPLACE(ip, '.', ''))) <> 3
or 
part1 = "invalid"
or 
part2 = "invalid"
or part3 = "invalid"
or part4 = "invalid"

order by invalid_count desc , ip desc