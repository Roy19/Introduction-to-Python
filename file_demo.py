#Name:			file_demo.py
#Date and Time:	05/10/2017 22:30(IST)
#Description:	A demo program in Python to demnstrate file handling operations

f=open("countries.txt","r")		#Define a file handler f open a file "countries.txt" in read mode

#Note:'line' variable here is not a list. But it can be used to iterate through
#the contents of the file 'countries.txt'(here)
for line in f:					#Iterate over the entire file contents
	line=line.strip()			#Strips extra newlines in the file.
	print(line)					#Print out the lines in the file
	
f.close()						#Always after finishing your work close the file 
								#to do some extra housekeeping!