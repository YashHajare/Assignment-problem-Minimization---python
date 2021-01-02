#################################################################
def Compute(mat1,copy_matrix):
    while (np.count_nonzero(mat1 == 0) != 0):
        #ROW Assignment
        print("3. ROW Assignment:")

        ##print(np.count_nonzero(mat1 == 0, axis=0))
        ##print(np.count_nonzero(mat1 == 0, axis=1))

        print("Note: '9999' means Assigned Value")
        print("Note: '1111' means Crossed Value")

        ##col_zeros = np.where(mat1[:,[0]] == 0)
        ##print("hsay",col_zeros)

        for i in range(mat1.shape[0]):
            if (np.count_nonzero(mat1[i] == 0) == 1):
                #finding row with one zero
                print("Assignmet in Row:", i + 1)
                row_temp = np.where(mat1[i] == 0)
        ##        print(temp[0])
                #Once found one single zero assigning it
                mat1[i][row_temp[0]] = 9999;

                if (np.count_nonzero(mat1[:,row_temp[0]] == 0) >= 1):
        ##            print("yasss where are they:",np.where(mat1[:,temp[0]] == 0))
                    for hey in range(mat1.shape[1]):
                        if (mat1[hey][row_temp[0]] == 0):
                            mat1[hey][row_temp[0]] = 1111        
        ##    else:
        ##        print(" ")

        print(mat1)
        print("----------------")   
        #ROW Assignment
        print("4. COL Assignment:")
        ##print("hsay:::",mat1[:,2][0])
        print("Note: '9999' means Assigned Value")
        print("Note: '1111' means Crossed Value")

        for j in range(mat1.shape[1]): #shape[1] for cols and shape[0] for rows
            if (np.count_nonzero(mat1[:,j] == 0) == 1):
                print("Assignment in Col:", j + 1)
                col_temp = np.where(mat1[:,j] == 0)
        ##        print(col_temp[0])
        ##        print(mat1[:,j][col_temp[0]])
                mat1[:,j][col_temp[0]] = 9999

                if (np.count_nonzero(mat1[col_temp[0]] == 0) >= 1):
                    for hey2 in range(mat1.shape[0]):
                        if (mat1[:,hey2][col_temp[0]] == 0):
                            mat1[:,hey2][col_temp[0]] = 1111
                
        print(mat1)
        print("----------------") 


    if (np.count_nonzero(mat1 == 0) == 0):
        #calculate cost
        temp_mat1 = mat1.copy()
        
        print("****Final answer****")
        mat1 = np.where(mat1 == 1111, "X", mat1)#we are changing data from int to str by putting '"X"'
        mat1 = np.where(mat1 == "9999", "[0]", mat1)#now matrix is converted into str dont put int lol
        print(mat1)
        costs = np.where(temp_mat1 == 9999)
        real_costs = costs[1]
        summ = 0
        print("Calculating costs:")
        for i in range(temp_mat1.shape[0]):
            print("A",i+1," Machine",i + 1 ," : ", copy_matrix[i][real_costs[i]])
            summ = summ + copy_matrix[i][real_costs[i]]
        print("Total Cost:", summ)
#######################################################################
import numpy as np

##mat1 = np.array([[10,12,19,11],
##                 [5,10,7,8],
##                 [12,14,13,11],
##                 [8,15,11,9]])

##mat1 = np.array([[8,28,17,11],
##                 [13,28,4,26],
##                 [38,19,18,15],
##                 [19,26,24,10]])

mat1 = np.array([[8,4,2,6,1],
                 [0,9,5,5,4],
                 [3,8,9,2,6],
                 [4,3,1,0,3],
                 [9,5,8,9,5]])

copy_matrix = mat1.copy();
print(mat1)
print("----------------")
print("Minimum in ROW : ", np.amin(mat1,axis=1))
print("Minimum in COL : ", np.amin(mat1,axis=0))
print("Shape :",mat1.shape)
print("----------------")
#ROW Subtraction
print("1. Step Row subtraction:")
for i in range(mat1.shape[0]):
##    print(mat1[i] - np.amin(mat1[i]))
    mat1[i] = mat1[i] - np.amin(mat1[i])
print(mat1)
print("----------------")

#COL Subtraction
print("2. Step Column subtraction:")
for j in range(mat1.shape[1]):
##    print(mat1[:,j] - np.amin(mat1[:,j]))
    mat1[:,j] = mat1[:,j] - np.amin(mat1[:,j])
print("1st Reduced matrix")
print(mat1)
print("----------------")

Compute(mat1,copy_matrix)
        
        

