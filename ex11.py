print("\nHow old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"\nSo, you're {age} old, {height} tall and {weight} heavy.")
print("So, you're %s old, %s tall and %s heavy" % (age, height, weight))
print("So, you're {} old, {} tall and {} heavy".format(age, height, weight))
print()
