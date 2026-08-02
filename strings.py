#1.
first = "Ada"
last = "Lovelace"

full_name = first + " " + last

print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(len(full_name))
print(full_name[0], full_name[-1])
#output
#ADA LOVELACE
#ada lovelace
#Ada Lovelace
#12
#A 
#2.
print(full_name[:3])
#output
#Ada
print(full_name[:full_name.index(" ")])
#output
#Ada
