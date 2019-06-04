def number_of_pallets(item_size, number_items):
    import math
    print(f"Your item size is {item_size}.")
    print(f"You have {number_items} items.")
    print("Pallet capacity is 100.")
    number_pallets = math.ceil(item_size * number_items / 100)
    print(f"That means you need {number_pallets} pallets. \n")

number_of_pallets(1, 100)

item_size = 5
number_items = 100

number_of_pallets(item_size, number_items)

number_of_pallets(2, 100 + 900)

number_of_pallets(item_size + 1, number_items + 100)

number_of_pallets(int(input("item size: ")), int(input("number of items: ")))

item_size = int(input("item size: "))
number_items = int(input("number of items: "))

number_of_pallets(item_size, number_items)
