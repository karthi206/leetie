// ──────────────────────────────────────────────────
// Problem  : 2666. Allow One Function Call
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/allow-one-function-call/
// Runtime  : 57 ms (beats 6%)
// Memory   : 53476000 (beats 63%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {

  let hasBeenCalled = false;
  let result;

  return function(...args) {
    if (!hasBeenCalled) {
      result = fn(...args);
      hasBeenCalled = true;
      return result;
    } else {
      return undefined;
    }
  }

};

let fn = (a,b,c) => (a + b + c);
let onceFn = once(fn);

console.log(onceFn(1,2,3)); // 6
console.log(onceFn(2,3,6)); // undefined