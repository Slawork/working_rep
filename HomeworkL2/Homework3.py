#Дан список 0 и 1. Необходимо вывести наибольшее количество единиц, которые стоят друг за другом.
nums = [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0]
current_count = 0
max_count = 0
for i in nums:
    if i == 1:
        current_count += 1
    else:
        current_count = 0
    if current_count > max_count:
        max_count +=1
print(max_count)



