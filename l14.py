import nums as nums


def find_max(nums):
    max_num = float("inf") # smaller than all other numbers
for num in nums:
    if num > max_num:
# (Fill in the missing line here)
    max_num += 1
return max_num