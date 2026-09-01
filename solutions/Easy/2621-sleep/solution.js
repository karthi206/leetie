// ──────────────────────────────────────────────────
// Problem  : 2621. Sleep
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/sleep/
// Runtime  : 54 ms (beats 0%)
// Memory   : 52152000 (beats 0%)
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