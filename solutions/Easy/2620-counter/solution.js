// ──────────────────────────────────────────────────
// Problem  : 2620. Counter
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/counter/
// Runtime  : 52 ms (beats 0%)
// Memory   : 52668000 (beats 0%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

function createCounter(start) {
  let count = start;
  return function() {
    return count++;
  }
}