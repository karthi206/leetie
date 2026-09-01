// ──────────────────────────────────────────────────
// Problem  : 2625. Flatten Deeply Nested Array
// Difficulty: Medium
// Tags     : N/A
// Link     : https://leetcode.com/problems/flatten-deeply-nested-array/
// Runtime  : 148 ms (beats 34%)
// Memory   : 89096000 (beats 50%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function(arr, depth) {
  const stack = [...arr.map(item => [item, depth])];
  const result = [];

  while (stack.length > 0) {
    const [item, depth] = stack.pop();

    if (Array.isArray(item) && depth > 0) {
      stack.push(...item.map(subItem => [subItem, depth - 1]));
    } else {
      result.push(item);
    }
  }

  return result.reverse();
};
