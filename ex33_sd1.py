def while_loop(limit,i,numbers):
    
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

        print("The numbers: ")
    
    return numbers

i = 0
numbers = [] 

while_loop(int(input("Enter a limit: ")),i,numbers)

for num in numbers:
    print(num)