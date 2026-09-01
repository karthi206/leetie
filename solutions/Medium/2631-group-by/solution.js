// ──────────────────────────────────────────────────
// Problem  : 2631. Group By
// Difficulty: Medium
// Tags     : N/A
// Link     : https://leetcode.com/problems/group-by/
// Runtime  : 115 ms (beats 32%)
// Memory   : 78248000 (beats 78%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((groups, ele)=>{
        const key = fn(ele);
       (groups[key]??=[]).push(ele)
       return groups
    }, {})
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */