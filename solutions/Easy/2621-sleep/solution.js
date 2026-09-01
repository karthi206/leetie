// ──────────────────────────────────────────────────
// Problem  : 2621. Sleep
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/sleep/
// Runtime  : 36 ms (beats 88%)
// Memory   : 52620000 (beats 91%)
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