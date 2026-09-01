// ──────────────────────────────────────────────────
// Problem  : 2637. Promise Time Limit
// Difficulty: Medium
// Tags     : N/A
// Link     : https://leetcode.com/problems/promise-time-limit/
// Runtime  : 57 ms (beats 21%)
// Memory   : 54640000 (beats 15%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        const originalFnPromise = fn(...args);

        const timeoutPromise = new Promise((_, reject) => {
            setTimeout(() => {
                reject('Time Limit Exceeded')
            }, t);
        })

        return Promise.race([originalFnPromise, timeoutPromise]);
    }
};