for i in range(1, 4):
    print("Outer loop:", i)

    for num in range(1, 11):
        if num % 2 == 0:
            print(num, "Even")
        else:
            print(num, "Odd")
            #output:
            #Outer loop: 1
            #1 Odd
            #2 Even
            #3 Odd
            #4 Even
            #5 Odd
            #6 Even
            #7 Odd
            #8 Even
            #9 Odd
            #10 Even
            #Outer loop: 2
            #1 Odd
            #2 Even
            #3 Odd
            #4 Even
            #5 Odd
            #6 Even
            #7 Odd
            #8 Even
            #9 Odd
            #10 Even
            #Outer loop: 3
            #1 Odd
            #2 Even
            #3 Odd
            #4 Even
            #5 Odd
            #6 Even
            #7 Odd
            #8 Even