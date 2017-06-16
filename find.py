def find(word, letter,index):
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1
word=raw_input("input the word   ")
letter=raw_input("letter to be searched")
index=raw_input("searh starting index")
i=find(str(word), str(letter),int(index))
if i==-1:
	print "letter not found"
else:
	print "letter is in the index",i
