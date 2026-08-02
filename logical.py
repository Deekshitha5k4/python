percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))

eligible = percentage > 75 and attendance > 90

print("Eligible for scholarship:", eligible)
#output
#Enter percentage: 82
#Enter attendance %: 95
#Eligible for scholarship: True