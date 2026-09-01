// ──────────────────────────────────────────────────
// Problem  : 2667. Create Hello World Function
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/create-hello-world-function/
// Runtime  : 58 ms (beats 6%)
// Memory   : 54060000 (beats 13%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────


var createHelloWorld = function() { 
    return function() {
        return "Hello World";
    }
}