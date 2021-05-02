import numpy as np
from numpy.linalg import inv
from numpy.linalg import det

try :
	R = int(input("Enter the number of rows : "))
	C = int(input("Enter the number of columns : "))
	matrix = []

	# Inputting Elements
	if R == C:
		for i in range(R):
		    r = []
		    for j in range(C):
		    	r.append(int(input("Enter Elements : ")))
		    matrix.append(r)

	A = np.array(matrix)
	print(A)
	DET = round(det(A))
	print("Determinant : " , DET)
	print("adjA :\n",DET*inv(A))


except:
	print("You have entered a Singular Matrix!")
