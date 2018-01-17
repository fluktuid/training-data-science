import sys

words = {}
for i in range(1,len(sys.argv)):
	word = sys.argv[i]
	word_in_list = 0
	if word in words:
		word_in_list = words[word]
	words.update({word:word_in_list+1})

print(words)
