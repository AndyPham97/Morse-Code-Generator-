from morsecodelib import *

def morse_code(x):
	
	x = x[1:len(x)-1]

	list = ""
	final = ""
	
	for i in range(len(x)):
		if x[i] == '.':
			list = list + "."
			if i == len(x)-1:
				if list in dict:
					final = final + dict[list]
					list = ""
					
		elif x[i] == '-':
			list = list + "-"
			if i == len(x)-1:
				if list in dict:
					final = final + dict[list]
					list = ""
			
		elif x[i] == ' ':
			if list in dict:
				final = final + dict[list]
				list = ""
		elif x[i] == '/':
			list = list + '/'
			
	return final

loop = 1	
while loop != 0:
	print()
	str = input("Enter in a morse code: ")
	str = '{' + str + '}'
	print()
	print(morse_code(str))
	print()
	retake = input("Would you like to go again? Type (Y) or (N): ")
	if retake == 'N' or retake == 'n':
		loop = 0
		print("Thank you for trying it out!\n")
	
				