# ──────────────────────────────────────────────────
# Problem  : 636. Exclusive Time of Functions
# Difficulty: Medium
# Tags     : Array, Stack
# Link     : https://leetcode.com/problems/exclusive-time-of-functions/
# Runtime  : 3 ms (beats 94%)
# Memory   : 19428000 (beats 26%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        callstack = []
        exectime = [0]*n

        for log in logs:
            idn, status, curtime = log.split(":")
            idn, curtime = int(idn), int(curtime)
            if status == "start":
                callstack.append([idn, curtime])

            else:
                x, y = callstack.pop()
                time = curtime - y + 1
                exectime[x] += time
                if callstack:
                    x, _ = callstack[-1]
                    exectime[x] -= time

        return exectime
                    




        