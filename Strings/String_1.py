#Input: 3
#       1
#       2
#       3

#Output: 123

#Input: 4
#       H
#       e
#       l           
#       l

#Output: Hell

user_input = input("Enter range number: ")
i = 0
j = ""
while i in range(int(user_input)):
    get = input()
    j += get
    i += 1
print(j)
