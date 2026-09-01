// ──────────────────────────────────────────────────
// Problem  : 2648. Generate Fibonacci Sequence
// Difficulty: Easy
// Tags     : N/A
// Link     : https://leetcode.com/problems/generate-fibonacci-sequence/
// Runtime  : 40 ms (beats 72%)
// Memory   : 54272000 (beats 14%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {

  let current = 0; 
  let next = 1;

  while (true) {
    yield current; 

    [current, next] = [next, current + next];

    // The above line is equivalent to the following:
    // let temp = current;
    // current = next;
    // next = temp + next;
  }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */