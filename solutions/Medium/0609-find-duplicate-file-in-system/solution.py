# ──────────────────────────────────────────────────
# Problem  : 609. Find Duplicate File in System
# Difficulty: Medium
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/find-duplicate-file-in-system/
# Runtime  : 19 ms (beats 65%)
# Memory   : 26288000 (beats 82%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for s in paths:             
            s = s.split(' ')                # parse the string: first component is   
            path = s.pop(0)                 # the path; the other components are files

            for file in s:
                idx = file.index('(')       # Build a dict of files with key = file content
                d[file[idx:]].append(path+'/'+file[:idx]) 

                                            # return the dict values for keys w/ > 1 files
        return [d[i] for i in d.keys() if len(d[i]) > 1]