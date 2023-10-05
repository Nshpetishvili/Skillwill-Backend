max_length = 0

#Input from the user for 5 strings and find the longest one
for i in range(5):
    userinput = input("Enter string {}: ".format(i + 1))
    length = len(userinput)
    if length > max_length:
        max_length = length

#Length of the longest string
print("The length of the longest string is:", max_length)