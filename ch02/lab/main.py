import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 3
cost_per_class = cost_per_week / classes_per_week
print("Your cost per class is",(cost_per_class))

print("weeks", int(weeks))
print("classes", int(classes))
print("tuition", int(tuition))
print("cost_per_week", float(cost_per_week))
print("classes_per_week", int(classes_per_week))
print("cost_per_class", float(cost_per_class))

#Part B
random_number = [1,3,5,7,9]
result = random.choice(random_number)
print(result)


