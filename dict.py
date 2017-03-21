from sys import argv

script, filename = argv
txt = open(filename)

#initializing data structures
dictionary = {}
synonym = {}

def addW(word,meaning):
	#adding word to Dictionary
	if word not in dictionary:
		dictionary[word] = meaning
	else:
		print "ERROR: Word already exists in dictionary!"

def addS(word1, word2):
	#adding synonym to Thesaurus
	if word1 not in synonym:
		synonym[word1] = word2
	else:
		if type(synonym[word1]) is list:
			synonym[word1] = synonym[word1] + [word2]
		else:
			synonym[word1] = [synonym[word1]] + [word2]

def lookW(word):
	#looking up word in dictionary
	if word in dictionary.keys():
		print word + ":" + dictionary[word]
	else:
		print "ERROR: Word not in dictionary!"

def lookS(word):
	#DFS connected components algorithm to look up synonym
	stack = []
	stack += [synonym[word]]

	visited = []

	while stack:
		vertex = stack.pop()

		if vertex not in visited:
			visited.append(vertex)

			if vertex in synonym.keys():
				stack += [synonym[vertex]]

	#flattening list of list
	for x in range(len(visited)):
		if type(visited[x]) is list:
			visited = sum(visited, [])

	#formatting visited list
	printS = ""
	for x in range(len(visited)):
		printS = printS + str(visited[x])
		if x!=len(visited)-1:
			printS = printS + ','

	print word + ":" + printS 

line = txt.readline()

#scanning through the text file line by line
while line:

	#warsing when lines start with addWord
	if line.startswith('addWord'):
		word = line[line.index(':')+1:line.rindex(':')]
		meaning = line[line.rindex(':')+1:]
		meaning = meaning.replace("\n","")
		addW(word, meaning)

	#parsing when lines start with addSynonym
	if line.startswith('addSynonym'):

		word1 = line[line.index(':')+1:line.rindex(':')]
		word2 = line[line.rindex(':')+1:]
		word2 = word2.replace("\n","")
		addS(word1, word2)

	#parsing when lines start with lookupWord
	if line.startswith('lookupWord'):

		word = line[line.rindex(':')+1:]
		word = word.replace("\n","")
		
		if word not in synonym:
			print "ERROR: word does not exist in Theraurus."
		else:
			lookW(word)

	#parsing when lines start with lookupSynonyms
	if line.startswith('lookupSynonyms'):

		word = line[line.rindex(':')+1:]
		word = word.replace("\n","")
		lookS(word)

	line = txt.readline()

txt.close()
