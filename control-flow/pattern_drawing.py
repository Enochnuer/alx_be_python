size_of_pattern = int(input("Enter the size of the pattern:"))
while size_of_pattern >= 0:
    for i in range(1,size_of_pattern + 1 ):
        for j in range(1,size_of_pattern + 1):
            print("*", end=" ")
        print()
     