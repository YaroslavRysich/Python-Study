from traceback import print_list

list_one = []
list_two = ['Glory '  'To '  'Ukraine '  'Forever '  'Glory ']

for i in range(5):
 list_one.insert(i, input("Please input data for include to list: "))

print("List One:", list_one)
print("List Two:", list_two)

list_two.extend(list_one)

print("Combination of two lists:", list_two)