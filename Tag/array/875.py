class Solution:
	def minEatingSpeed(self, piles: List[int], H: int) -> int:
		left, right = 1, max(piles)
		while left < right:
			mid = (left + right) // 2
			if self.sum_res(piles, mid) > H:
				left = mid + 1
			else:
				right = mid
		return left

	def sum_res(self, piles, speed):
		res = 0
		for one in piles:
			res += (one + speed - 1) // speed
		return res

'''
sum += (pile + speed - 1) / speed
写成 sum += pile / speed; 是下取整，为了把下取整改成上取整（根据题目要求需要上取整）。

因此，我们需要在分子加上「分母的值 - 1」，这样就可以改变默认 / 下取整的行为。

所以应该看做 pile + (speed - 1) 
'''