# Палиндром
# 13431

def palindrom(s):
    for i in range(len(s)//2):  # от 0 до 2
        left = i
        right = len(s) - i - 1
        if s[left] != s[right]:
            return False
    return True


s = input("Введите текст: ").lower()
print(palindrom(s))


def decision(nums):
    sum_nums = sum(nums)
    real_sum = sum(list(range(max(nums)+1)))
    return real_sum - sum_nums

print(decision([9, 6, 4, 2, 3, 5, 7, 0, 1]))


def decision(nums):
    value = [i for i in range(min(nums), max(nums))]
    for i in value:
        if i not in nums:
            return i


print(decision([9, 6, 4, 2, 3, 5, 7, 0, 1]))