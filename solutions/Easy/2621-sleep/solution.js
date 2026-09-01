// ──────────────────────────────────────────────────
// Problem  : 2621. Sleep
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/sleep/
// Runtime  : 64 ms (beats 6%)
// Memory   : 53768000 (beats 37%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {number} millis
 */
async function sleep(millis) {
    await new Promise(resolve => setTimeout(resolve, millis));
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */