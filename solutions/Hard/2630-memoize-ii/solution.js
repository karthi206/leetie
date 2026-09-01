// ──────────────────────────────────────────────────
// Problem  : 2630. Memoize II
// Difficulty: Hard
// Tags     : N/A
// Link     : https://leetcode.com/problems/memoize-ii/
// Runtime  : 290 ms (beats 33%)
// Memory   : 121032000 (beats 44%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

const RES = Symbol("result");

/**
 * @param {Function} fn
 */
function memoize(fn) {
    const globalCache = new Map();

    return (...params) => {
        let currentCache = globalCache;
        for(const param of params) {
            if (!currentCache.has(param)) {
                currentCache.set(param, new Map());
            }
            currentCache = currentCache.get(param);
        }

        if (currentCache.has(RES)) return currentCache.get(RES);

        const result = fn(...params);

        currentCache.set(RES, result);
        return result;
    }
}