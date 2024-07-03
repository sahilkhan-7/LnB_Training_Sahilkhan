numbers = [i for i in range(1, 21)]
print(numbers)

new_list = numbers[0:5] + numbers[-5:]
print(f"New list: {new_list}")

square_list = [i**2 for i in new_list]
print(f"Square list: {square_list}")

# Splitting the new list into three parts and copying them to new lists
l1 = new_list[0:2].copy()
l2 = new_list[2:5].copy()
l3 = new_list[5:].copy()
print(f"List 1: {l1}")
print(f"List 2: {l2}")
print(f"List 3: {l3}")