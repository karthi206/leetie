// ──────────────────────────────────────────────────
// Problem  : 2649. Nested Array Generator
// Difficulty: Medium
// Tags     : N/A
// Link     : https://leetcode.com/problems/nested-array-generator/
// Runtime  : 138 ms (beats 85%)
// Memory   : 89956000 (beats 41%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

var inorderTraversal = function*(arr) {
    for (let element of arr) {
        if (Array.isArray(element)) {
            yield* inorderTraversal(element);
        } else {
            yield element;
        }
    }
};