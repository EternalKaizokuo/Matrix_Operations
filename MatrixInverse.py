import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

try :
	R = int(input("Enter the number of rows : "))
	C = int(input("Enter the number of columns : "))
	matrix = []

	# Getting elements as input from user
	if R == C:
		for i in range(R):
		    r = []
		    for j in range(C):
		    	r.append(int(input("Enter Elements : ")))
		    matrix.append(r)

	# Converting the list into a Numpy Array
	A = np.array(matrix)
	print('Matrix A :\n',A)

	# I've found Determinant and Adjoint separately because that's how my teacher wants the answers written
	#### Inverse = (1/Determinant)*Adjoint
	DET = round(det(A))
	INV = inv(A)
	print("Transpose of A:\n",A.T)
	print("Determinant of A: " , DET)
	print("Adjoint of A :\n",DET*INV)

# Singular matrixes don't have inverse i.e their Determinant is 0
except:
	print("You have entered a Singular Matrix!")
