# Python script to take a list of names and generate possible username formats
# Expects a list of names in format 'FIRSTNAME SURNAME'
# sh3llcmdr
# 20/07/2016

from sys import argv

#ask for list of usernames and open file
usernames = open(argv[1])

#open the output file
output_file = open('mangled_usernames.txt', 'w')

#for each line of the file
for names in usernames:
	#find first name
	names = names.strip('\n')
	both_names_cut = names.split(" ")
	first_name = both_names_cut[0]
	#find surname
	surname = both_names_cut[1]
	#first_letter = first_name[:1]
	
	#print first_name
	#print surname
	#print first_letter
	#print("\n")

	#format changes
	#letter of first name, surname
	#bjones
	output_file.write(str(first_name[:1] + surname).lower() + "\n")

	#first name.surname
	#bob.jones
	output_file.write(str(first_name + "." + surname).lower() + "\n")

	#surname then first letter of first name
	#jonesb
	output_file.write(str(surname + first_name[:1]).lower() + "\n")

	#first name.surname
	#b.jones
	output_file.write(str(first_name[:1] + "." + surname).lower() + "\n")

	##first letter of first name, first letter of surname
	##bj
	#output_file.write(first_name + "." + surname)

