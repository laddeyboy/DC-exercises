my_list = [1,2,3,4,5,6]

#Sum the Numbers
sum_total = 0
for nums in my_list:
    sum_total += nums
print("Sum Total is: {}".format(sum_total))

#Larget Number
my_list = [3,5,87,2,8,1]
my_list.sort()
print("Largest Number is: {}".format(my_list.pop()))

#Smallest Number
my_list = [3,5,87,2,8,1]
my_list.sort()
print("Smallest Number is: {}".format(my_list[0]))

#Even Number
my_list = [3,5,87,2,8,1]
print("Even Number List: ")
for x in my_list:
    if(x % 2 == 0):
        print(x)
        
#Positive Number
my_list = [-3,5,-87,2,8,-1]
print("Positive Numbers: ")
for x in my_list:
    if(x > 0):
        print(x)
        
#Positive Number List
my_list = [-3,5,-87,2,8,-1]
new_list = []
for x in my_list:
    if(x > 0):
        new_list.append(x)
print("My Positive Int List: {}".format(new_list))

#Mulitply a List
my_list = [2,4,6,5,3,1]
single_factor = 2
new_list = []
for num in my_list:
    new_list.append(num * single_factor)
print("Multiplication List is: {}".format(new_list))

#Vector Multiply
vector1 = [2,4,5]
vector2 = [2,3,6]
new_list = []
x = 0
while x < len(vector1):
    new_list.append(vector1[x] * vector2[x])
    x += 1
print("Multiply Vector List: {}".format(new_list))

#Matrix Addition
matrix1 = [[1,3],[2,4]]
matrix2 = [[5,2],[1,0]]
new_matrix = []
for x in range(len(matrix1)):
    for y in range(len(matrix1[0])):
        new_matrix.append(matrix1[x][y] + matrix2[x][y])
print("Here is your added Matrix: ")
print(new_matrix)

#Matrix Addition II
matrix1 = [[1,3],[2,4],[6,7]]
matrix2 = [[5,2],[1,0],[8,9]]
new_matrix = []
for x in range(len(matrix1)):
    for y in range(len(matrix1[0])):
        new_matrix.append(matrix1[x][y] + matrix2[x][y])
print("Here is your added Matrix: ")
print(new_matrix)

#De-Dup
my_list = [1, 2, 2, 3, 4, 4, 5]
#my_list = ['one', 'two', 'two', 'three', 'four', 'four', 'five']
new_list = set(my_list)
print("Here is your de-dup list: {}".format(new_list))

#Matrix Multiplication




               