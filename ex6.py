types_of_people = 10
x = f"There are {types_of_people} types of people." #1

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #2

print(x)
print(y)

print(f"I said: {x}") # 3
print(f"I also said: '{y}'") # extra single quotes? #4

hilarious = False
joke_evalution = "Isn't that joke so funny?! {}"

print(joke_evalution.format(hilarious))  # 5!

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
