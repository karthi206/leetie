// ──────────────────────────────────────────────────
// Problem  : 2623. Memoize
// Difficulty: Medium
// Tags     : N/A
// Link     : https://leetcode.com/problems/memoize/
// Runtime  : 58 ms (beats 0%)
// Memory   : 53780000 (beats 0%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {Function} fn
 */
function memoize(fn) {
    
   const cache = {};
  
   return function(...args) {
    const key = JSON.stringify(args);
    
    if (key in cache) {
      return cache[key];
    }
    
    const result = fn.apply(this, args);
    cache[key] = result;
    
    return result;
  }
  
}


const memoizedSum = memoize(function(a, b) {
  return a + b;
});

console.log(memoizedSum(2, 3)); // Output: Computing sum, 5
console.log(memoizedSum(2, 3)); // Output: 5