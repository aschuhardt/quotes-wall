import os

#get working directory
os.chdir(os.path.dirname(__file__))
mydir = os.getcwd()

#set path of input (plaintext) file
input_filename = mydir + '/../static/quotes.txt'

#set path of output (pugjs) file
output_filename = mydir + '/../static/quotes.pug'

#delete existing pug file
if os.path.isfile(output_filename):
	os.remove(output_filename)

#set up header of pugjs file
pug_contents = 'doctype html'
pug_contents += '\nhtml'
pug_contents += '\n\thead'
pug_contents += '\n\t\tlink(rel=\'stylesheet\', href=\'/styles/style.css\')'
pug_contents += '\n\tbody'
pug_contents += '\n\t\t'

#open input (plaintext) file
with open(input_filename, 'r+') as f:

	#create a list to store lines in
	lines = list()
	quotes = list()
	authors = list()
	#iterate through each line in the input file
	for line in f:
		line = line.strip(' ').strip('\n').replace('"', '&quot;')
		if line != '':
			if line.startswith('-'):
				print('found author "' + line + '"\n')
				authors.append(line)
			else:
				print('found quote "' + line + '"\n')
				quotes.append(line)
	#reverse lists
	quotes = list(reversed(quotes))
	authors = list(reversed(authors))
	#add quotes + authors to list in correct order
	for i in range(len(quotes)):
		lines.append(quotes[i])
		lines.append(authors[i])
	for line in lines:
		#assign a css class to line based on whether it starts
		#	with a hyphen or not
		pclass = 'author' if line.startswith('-') else 'quote'
		#skip empty lines
		if line != '\n':
			#add contents of line to output text
			pug_contents += '\n\t\t\tp(class=\'' + pclass + '\') ' + line

#open/create the output (pugjs) file
with open(output_filename, 'w+') as pug:
	#write the constructed pugjs content to the output file
	pug.write(pug_contents)
