import csv

##### VARIABLES AND FILE NAMES #####

#File to read
fileName ='sample.csv'

#File to create
newFileName = 'newFileName.csv'

#Header for new file
header=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7']


##### OPEN FILE TO READ #####

#Open csv file
myCSVFile = open(fileName, 'rb')

#OPTIONAL: Skip first line (header):
next(myCSVFile)

myFile =csv.reader(myCSVFile)


##### CREATE FILE TO WRITE  ####

#Create new csv file and make it appendable
#other options: w = overwrite, r = read, a = append, ab = append binary.
csvFile = open(newFileName,'ab')

newFile =csv.writer(csvFile)

#write header to new file
newFile.writerow(header)


##### LOOP OVER FILE ####

#Optional: skip first line
firstLine= True

#Loop over csv rows
for row in myFile:

	#Optional: Skip first line
	if firstLine:
		firstLine=False
		continue

	## DO STUFF WITH EACH ROW OR VALUE ##

	#Print value in particular column
	print(row[2])

	#Print entire row
	print(row)	

	#append a new value to end of row
	row.append("MyNewValue")

	#Write entire row to another file
	newFile.writerow(row)

	

#####CLOSE THE FILES####
#####After looping though file once, close it and re-open to loop through it again, or use "with" loop.

myCSVFile.close()
csvFile.close()


