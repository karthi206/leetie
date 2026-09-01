// ──────────────────────────────────────────────────
// Problem  : 2634. Filter Elements from Array
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/filter-elements-from-array/
// Runtime  : 44 ms (beats 53%)
// Memory   : 53556000 (beats 56%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let fil=[]
    for(let i=0;i<arr.length;i++){
        if(fn(arr[i],i)){
            fil.push(arr[i]);
        }
    }
    return fil
};