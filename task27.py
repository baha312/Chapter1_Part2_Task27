# Напишите функцию где исходный список содержит положительные и отрицательные числа. 
# Требуется положительные поместить в один список, а отрицательные - в другой.

all_ = [20, 35, 47, -12, -25, 98, -20, 10, -78]
print(all_)

positive_nums = []
negative_nums = []

for x in all_:
    if x >= 1:
        positive_nums.append(x)
    elif x <= -1:
        negative_nums.append(x)

print(positive_nums)
print(negative_nums)
