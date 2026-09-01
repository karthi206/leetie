// ──────────────────────────────────────────────────
// Problem  : 2618. Check if Object Instance of Class
// Difficulty: Medium
// Tags     : N/A
// Link     : https://leetcode.com/problems/check-if-object-instance-of-class/
// Runtime  : 69 ms (beats 74%)
// Memory   : 62532000 (beats 68%)
// Language : javascript
// Copyright: (c) 2026 karthi206. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

/**
 * @param {Object} object
 * @param {Function} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    while(obj!=null)
    {
        if(obj.constructor === classFunction)
        {
            return true;
        }

        obj = Object.getPrototypeOf(obj);

    }

    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */