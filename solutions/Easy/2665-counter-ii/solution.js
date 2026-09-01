// ──────────────────────────────────────────────────
// Problem  : 2665. Counter II
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/counter-ii/
// Runtime  : 58 ms (beats 16%)
// Memory   : 56276000 (beats 72%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

var createCounter = function(init) {
  let presentCount = init;

  function increment() {
    return ++presentCount;
  }

  function decrement() {
      return --presentCount;
  }

  function reset() {
      return (presentCount = init);
  }

  return { increment, decrement, reset };
};