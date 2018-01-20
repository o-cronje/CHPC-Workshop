import numpy as np
import matplotlib.pyplot as pl
import math
import glob
alldays = glob.glob("*day.csv")

counter1 = 0
counter2 = 0
max_data = np.zeros([7,4])
min_data = np.zeros([7,4])
mean_data = np.zeros([7,4])

for filename in alldays:
	dataarray = np.loadtxt(filename,delimiter = ",",skiprows = 1, usecols = (1,2,3,4))
	transpose_data = np.transpose(dataarray)
	#print(dataarray)
	counter2 = 0
	for cols in transpose_data:
		print(max_data)
		#print(cols)
		max_data[counter1][counter2] = np.amax(cols)
		min_data[counter1][counter2] = np.min(cols)
		mean_data[counter1][counter2] = np.mean(cols)
		counter2 = counter2 + 1
	counter1 = counter1 + 1

print(max_data)
print(min_data)
print(mean_data)

d = np.linspace(0,6,7)
print(d)

pl.subplot(2,2,1) 	#pl.subplot(rows,columns,place)
pl.plot(d,max_data[:,0],"r.-")
pl.plot(d,mean_data[:,0],"y-")
pl.plot(d,min_data[:,0],"b-*")
pl.xlabel("day")
pl.ylabel("Temp${}^0C$")
#pl.xlim(xmax=24,xmin=10)
pl.legend(["max","mean","min"])
pl.title("Temperature")


pl.subplot(2,2,2) 	#pl.subplot(rows,columns,place)
pl.plot(d,max_data[:,1],"r.-")
pl.plot(d,mean_data[:,1],"y-")
pl.plot(d,min_data[:,1],"b-*")
pl.xlabel("day")
pl.ylabel("Pressure")
pl.ylim(ymax=1.5,ymin=0.1)
pl.legend(["max","mean","min"])
pl.title("Pressure")


pl.subplot(2,2,3) 	#pl.subplot(rows,columns,place)
pl.plot(d,max_data[:,2],"r.-")
pl.plot(d,mean_data[:,2],"y-")
pl.plot(d,min_data[:,2],"b-*")
pl.xlabel("day")
pl.ylabel("Knots")
pl.ylim(ymax=22,ymin=-2)
pl.legend(["max","mean","min"])
pl.title("Wind Speed")


pl.subplot(2,2,4) 	#pl.subplot(rows,columns,place)
pl.plot(d,max_data[:,3],"r.-")
pl.plot(d,mean_data[:,3],"y-")
pl.plot(d,min_data[:,3],"b-*")
pl.xlabel("day")
pl.ylabel("Degrees")
pl.ylim(ymax=400,ymin=100)
pl.legend(["max","mean","min"])
pl.title("Wind Direction")

pl.show()













