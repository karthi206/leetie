# ──────────────────────────────────────────────────
# Problem  : 659. Split Array into Consecutive Subsequences
# Difficulty: Medium
# Tags     : Array, Hash Table, Greedy, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Runtime  : 23 ms (beats 86%)
# Memory   : 20504000 (beats 17%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
	def isPossible(self, nums: List[int]) -> bool:

		if len(nums) < 3: return False

		frequency = collections.Counter(nums)
		subsequence = collections.defaultdict(int)

		for i in nums:

			if frequency[i] == 0:
				continue

			frequency[i] -= 1

			# option 1 - add to an existing subsequence
			if subsequence[i-1] > 0:
				subsequence[i-1] -= 1
				subsequence[i] += 1

			# option 2 - create a new subsequence 
			elif frequency[i+1] and frequency[i+2]:
				frequency[i+1] -= 1
				frequency[i+2] -= 1
				subsequence[i+2] += 1

			else:
				return False

		return True

	# TC: O(n), SC: O(n)