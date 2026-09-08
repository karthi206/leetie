# ──────────────────────────────────────────────────
# Problem  : 493. Reverse Pairs
# Difficulty: Hard
# Tags     : Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
# Link     : https://leetcode.com/problems/reverse-pairs/
# Runtime  : 823 ms (beats 77%)
# Memory   : 26264000 (beats 97%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        arr[low:high + 1] = temp

    def countpairs(self, arr, low, mid, high):
        right = mid + 1
        cnt = 0

        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            cnt += (right - (mid + 1))

        return cnt

    def mergesort(self, arr, low, high):
        cnt = 0

        if low >= high:
            return cnt

        mid = (low + high) // 2

        cnt += self.mergesort(arr, low, mid)
        cnt += self.mergesort(arr, mid + 1, high)
        cnt += self.countpairs(arr, low, mid, high)
        self.merge(arr, low, mid, high)

        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergesort(nums, 0, len(nums) - 1)