# Write a Python program to check if two given sets have no elements in common.

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}
print("Original set elements:")
print(x)
print(y)
print(z)

compare_x_y = x.isdisjoint(y)
compare_y_z = y.isdisjoint(z)
compare_x_z = x.isdisjoint(z)
print("\nConfirm two given sets have no element(s) in common:")
print('x and y: ', compare_x_y)
print('y and z: ', compare_y_z)
print('x and z: ', compare_x_z)

# Write a Python program to remove the intersection of a 2nd set from the 1st set.

sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(sn1)
print(sn2)

sn1.difference_update(sn2)
print(sn1)

