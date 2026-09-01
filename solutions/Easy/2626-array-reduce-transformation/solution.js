// ──────────────────────────────────────────────────
// Problem  : 2626. Array Reduce Transformation
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/array-reduce-transformation/
// Runtime  : 34 ms (beats 0%)
// Memory   : 52288000 (beats 0%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let result = init; // Start with the initial value
    for (let i = 0; i < nums.length; i++) {
        result = fn(result, nums[i]); // Apply the reducer function sequentially
    }
    return result; // Return the final accumulated value
};