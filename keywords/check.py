import keyword
word = input("Enter a word: ")
if keyword.iskeyword(word):
    print(word, "is a Python keyword")
else:
    print(word, "is not a Python keyword")
   # Enter a word: class
#class is a Python keyword