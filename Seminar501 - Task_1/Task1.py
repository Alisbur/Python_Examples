nums = [1, 2, 3, 5]

for i in range(1, len(nums)):
    if nums[i-1] != nums[i]-1:
        print(f"не хватает числа {nums[i - 1] + 1}")
        break
