// ──────────────────────────────────────────────────
// Problem  : 2650. Design Cancellable Function
// Difficulty: Hard
// Tags     : N/A
// Link     : https://leetcode.com/problems/design-cancellable-function/
// Runtime  : 52 ms (beats 50%)
// Memory   : 53520000 (beats 63%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    var cancelled = false;
    var cancel;
    const cancelPromise = new Promise((_, reject) => cancel = () => {
            cancelled = true;
            reject("Cancelled");
        });
    
    const promise = (async () => {
        let next = generator.next();
        while (!cancelled && !next.done) {
            try {
                next = generator.next(await Promise.race([next.value, cancelPromise]));
            } catch (e) {
                next = generator.throw(e);
            }
        }

        return next.value;
    })();
    return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */