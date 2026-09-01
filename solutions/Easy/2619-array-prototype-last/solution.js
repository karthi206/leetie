// ──────────────────────────────────────────────────
// Problem  : 2619. Array Prototype Last
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/array-prototype-last/
// Runtime  : 34 ms (beats 92%)
// Memory   : 53964000 (beats 19%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

Array.prototype.last = function() {
  if (this.length === 0) {
    return -1;
  } else {
    return this[this.length - 1];
  }
};