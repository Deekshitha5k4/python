
values = input("Enter numbers separated by spaces: ")
 
numbers = list(map(int, values.split()))


print("Sum:", sum(numbers))
#output:
#Enter numbers separated by spaces: 12 13
#Sum: 25