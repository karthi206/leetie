// ──────────────────────────────────────────────────
// Problem  : 2635. Apply Transform Over Each Element in Array
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/apply-transform-over-each-element-in-array/
// Runtime  : 41 ms (beats 71%)
// Memory   : 53684000 (beats 49%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

var map = function(arr, fn) {
    for (let i = 0; i < arr.length; ++i) {
        arr[i] = fn(arr[i], i);
    }
    return arr;
};