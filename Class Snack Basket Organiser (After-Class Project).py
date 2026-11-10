basket1 = {"muffins", "croissant", "chips", "sandwich", "muffins"}
basket2 = {"cookies", "pastry", "ice cream", "pastry", "cheesecake"}
print("Basket 1: ", basket1)
print("Basket 2: ", basket2)

basket1.add("pizza")
print("Basket 1 after adding pizza: ", basket1)

common_snacks = basket1.intersection(basket2)
print("Snacks in both baskets: ", common_snacks)

import array as arr
snacks_counts = arr.array('i', [3, 5, 4, 1])
print("Snacks counts array: ", snacks_counts)

snacks_counts.insert(1, 0)
snacks_counts.append(5)
print("Snacks a\counts after adding new snacks: ", snacks_counts)
count_of_4 = snacks_counts.count(4)

snacks_counts.reverse()
print("Reversed snacks counts array: ", snacks_counts)

print("")
print("==================================================")
print("========== CLASS SNACK BASKET ORGANIZER ==========")
print("Basket 1: ", basket1)
print("Basket 2: ", basket2)
print("Shared fruits: ", common_snacks)
print("Fruit counts: ", snacks_counts)
print("==================================================")