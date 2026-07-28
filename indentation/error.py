from re import match


age = 18

if age >= 18:
    print("You are an adult")
   print("You can vote")
else:
    print("You are a minor")
#IndentationError: unindent does not match any outer indentation level
age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")
else:
    print("You are a minor")