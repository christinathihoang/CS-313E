#   File: htmlChecker.py
#   Description: This program checks a file and reports if the tags are correctly matched or not.
#   Student's Name: Christina Hoang
#   Student's UT EID: ch42297
#   Course Name: CS 313E
#   Unique Number: 86940
#
#   Date Created: 6/28/2017
#   Date Last Modified: 6/30/2017


# this function sorts through the file and returns all found tags
def getTag(line):
	tag = ""
	tagList = []
	flag = False

	# iterates through each character in each line in the file
	for ch in line:

		# locates a tag
		if ch == "<":
			flag = True

		# appends found tags to the list of tags
		elif (ch == ">" or ch == " ") and flag:
			tagList.append(tag)
			tag = ""
			flag = False

		# creates a new tag
		if ch != "<" and ch != " " and flag:
			tag += ch

	# returns a list of tags if it isn't empty
	if len(tagList) != 0:
		return(tagList)

# this function returns True for two matching tags
def matches(openTag, closeTag):
	return(openTag == closeTag)

# this function checks that each tag has a matching tag
def tagChecker(tagList):
	s = Stack()
	validTags = []
	exceptions = []

	while len(tagList) != 0:
		tag = tagList.pop(0)

		# make exceptions for tags that do not need to match
		if tag == "meta" or tag == "hr" or tag == "br":
			print("Tag",tag,"does not need to match: stack is still", str(s))
			if tag not in exceptions:
				exceptions.append(tag)

		# find starting tag
		elif tag[0] != "/":
			s.push(tag)
			print("New tag",tag,"found and added to list of valid tags")
			print("Tag",tag,"pushed: stack is now",str(s))

		# match starting tag with ending tag
		else:
			top = s.peek()
			if matches(tag[1:], top):
				if top not in validTags:
					validTags.append(s.pop())
					validTags.append(tag)
					print("Tag",tag,"matches top of stack: stack is now",str(s))
				else:
					s.pop()
					print("Tag",tag,"matches top of stack: stack is now",str(s))
			else:
				print("Error: tag is",tag,"but top of stack is",s.peek())
				return
		

	# sort tags
	validTags.sort()
	exceptions.sort()

	# print results of matching
	if s.isEmpty():
		print("Processing complete. No mismatches found.")
		return(validTags, exceptions)
	else:
		print("Processing complete. Unmatched tags remain on stack:", str(s))
		return(validTags, exceptions)

class Stack (object):
	def __init__(self):
		self.items = []

	def isEmpty (self):
		return(self.items == [])

	def push (self, item):
		self.items.append (item)

	def pop (self):
		return(self.items.pop())

	def peek (self):
		return(self.items[len(self.items)-1])

	def size (self):
		return(len(self.items))

	def __str__ (self):
		return("[{0}]".format(", ".join(str(i) for i in self.items)))


def main():
	# open file
	infile = open("htmlfile.txt","r")
	tagList = []
	
	# find all tags in the file and append to list
	for line in infile:
		if getTag(line) != None and getTag(line) != " ":
			tagList += getTag(line)

	# close file
	infile.close()
	
	# print list of tags
	print("tagList =", "[{0}]".format(", ".join(str(i) for i in tagList)))
	print("\n")

	# check that each tag has a match
	validTags, exceptions = tagChecker(tagList)

	# print valid tags and exceptions
	print("\n")
	print("VALIDTAGS =", "[{0}]".format(", ".join(str(i) for i in validTags)))
	print("EXCEPTIONS =", "[{0}]".format(", ".join(str(i) for i in exceptions)))
main()