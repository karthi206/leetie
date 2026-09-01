// ──────────────────────────────────────────────────
// Problem  : 2627. Debounce
// Difficulty: Medium
// Tags     : N/A
// Link     : https://leetcode.com/problems/debounce/
// Runtime  : 53 ms (beats 39%)
// Memory   : 53900000 (beats 66%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

var debounce = function(fn, t = 1000) {
    let timer;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    }
};