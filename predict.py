import numpy as np
import os.path
from os import path

def return_prize(theta_0, theta_1, x):
	return theta_0 + theta_1 * x

def verif():
	if path.exists("thetas.csv") == False:
		print("thetas.csv doesn't exist, creating it with zero values for thetas")
		f = open("thetas.csv", "w")
		f.write("0")
		f.write("\n")
		f.write("0")
		f.close()
	data1 = np.loadtxt("thetas.csv", dtype = np.str)
	check = data1
	if (len(data1) != 2):
		return(0)
	for i in range(0,len(data1)):
		dotcount = 0
		for j in range(0,len(check[i])):
			if check[i][j].isdigit() == False and check[i][j]!= "." and (check[i][j]!= "-") and (check[i][j]!= "+"):
				return(0)
			if check[i][j]== "-" or check[i][j]== "+":
				if j != 0:
					return(0)
			if check[i][j] == ".":
				dotcount +=1
			if dotcount > 1:
				return(0)
	return(1)

def main():
	
	if verif() == 0:
		print("Bad CSV")
		return(0)
	theta = np.loadtxt("thetas.csv", dtype = np.longdouble)
	try:
		mileage = np.longdouble(input("Enter mileage:"))
	except:
		print ("Error")
		exit()
	if mileage < 0:
		mileage = 0
	value = return_prize(theta[0], theta[1], mileage)
	if value < 0:
		value = 0
	print(value)
	return

if __name__ == "__main__":
	main()
