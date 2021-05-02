import numpy as np

# Input for Matrix A
Ar = int(input("Enter the number of rows : "))
Ac = int(input("Enter the number of columns : "))
matrixA = []
# For user input
for i in range(Ar):
    r = []
    for j in range(Ac):
    	r.append(int(input("Enter Elements : ")))
    matrixA.append(r)

# Converting list into Numpy Array
numA = np.array(matrixA)



#Input for Matrix B
Br = int(input("Enter the number of rows :"))
Bc = int(input("Enter the number of columns :"))
matrixB = []
# For user input
for k in range(Br):
    r = []
    for l in range(Bc):
    	r.append(int(input("Enter Elements : ")))
    matrixB.append(r)

# Converting list into Numpy Array
numB = np.array(matrixB)


# np.matmul multiplies 2 matrixes
# But it would only work if the number of colums for matrix A = number of rows of matrix B
# Resultant matrix has number of rows of matrix A & number of columns of Matrix B
if Ac == Br:
	RESULT = np.matmul(numA,numB)
	print("\nAnswer : \n",RESULT)

else:
	print("The matrices can't be Multiplied because their orders aren't compatible")
