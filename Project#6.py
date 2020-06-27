# temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
# new_temp = [temp + 20 for temp in temperatures]
# print(new_temp)

x_values_1 = [2*index for index in range(5)]
x_values_2 = [2*index + 0.8 for index in range(5)]

print(x_values_1)
print(x_values_2)

x_values_midpoints = [(x1 + x2)/2.0 for (x1, x2) in zip(x_values_1, x_values_2)]
print(x_values_midpoints)

zip([1, 2, 3], [4, 6, 8])
