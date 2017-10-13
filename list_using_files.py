#Name:				list_using_files.py
#Date and Time:		05/10/2017 22:41(IST)
#Description:		This creates an empty list called countries and fills it up with
#					the names of the countries in the file 'countries.txt'

f = open("countries.txt" , "r")

countries=[]

for line in f:
	line = line.strip()
	countries.append(line)		#Append to the 'countries' list the name of the new country
	
f.close()

print(countries)				#Print out the list of countries.
print("")
print("The size of the list: "+str(len(countries)))			#print out the length of the list.
