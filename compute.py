import matplotlib.pyplot as plt
import numpy as np
import os.path
from os import path

def standardize(x):
	return (x - np.mean(x)) / np.std(x)

def destandardize(x, x_ref):
	return x * np.std(x_ref) + np.mean(x_ref)

def calculate_theta(lendata, thetas, x, y):
	sumtop = 0
	sumbottom = 0
	meanx = np.mean(x)
	meany = np.mean(y)
	for i in range(0, lendata):
		sumbottom += (x[i] - meanx) * (x[i] - meanx)
		sumtop += (x[i] - meanx) * (y[i] - meany)
		thetas [0,0] = sumtop / sumbottom
		thetas [0,1] = meany - thetas[0,0] * meanx
	return thetas

def verif():
	if path.exists("data.csv"):
		data1 = np.loadtxt("data.csv", dtype = np.str)
		check = data1
		for i in range(1,len(data1)):
			delimiter = 0
			dotcount = 0
			for j in range(0,len(check[i])):
				if check[i][j].isdigit() == False and check[i][j]!= "," and check[i][j]!= ".":
					print("Bad CSV")
					return(0)
				if check[i][j] == ",":
					delimiter +=1
					dotcount = 0
				if check[i][j] == ".":
					dotcount +=1
				if dotcount > 1:
					print("Bad CSV")
					return(0)
			if delimiter != 1:
				print("Bad CSV")
				return(0)
		return(1)
	print("No CSV named data.csv")
	return(0)

def decimal_str(x: float, decimals: int = 10) -> str:
    return format(x, f".{decimals}f").lstrip().rstrip('0')

def main():
	if verif():
		data = np.loadtxt("data.csv", dtype = np.longdouble, delimiter = ',', skiprows = 1)
		thetas = np.zeros((1, 2))
		x = standardize(data[:, 0])
		y = standardize(data[:, 1])
		thetas = calculate_theta(len(data), thetas, x, y)
		plt.plot(data[:, 0], data[:, 1], '.')
		plt.ylabel("Price")
		plt.xlabel("Km")
		y = thetas[0, 1] + thetas[0, 0] * x
		x = destandardize(x, data[:, 0])
		y = destandardize(y, data[:, 1])
		a = (y[0] - y[1]) / (x[0] - x[1])
		b = y[0] - a * x[0]
		a = decimal_str(a)
		b = decimal_str(b)
		thetas = [b, a]
		plt.plot(x, y)
		plt.show()
		f = open("thetas.csv", "w")
		f.write(thetas[0])
		f.write("\n")
		f.write(thetas[1])
		f.close()
	return

if __name__ == "__main__":
	main()
