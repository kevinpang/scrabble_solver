from itertools import permutations
from time import time
from string import ascii_lowercase

class Node(object):
	# Represents a node in a trie
	
	def __init__(self):
		self.children = {}
		self.terminal = False
	
	def insert(self, word):
		current_node = self
		
		for char in word:
			if not char in current_node.children:
				current_node.children[char] = Node()
				
			current_node = current_node.children[char]
			
		current_node.terminal = True
		
	def find(self, word):
		current_node = self
		
		for char in word:
			if not char in current_node.children:
				return False
				
			current_node = current_node.children[char]
				
		return current_node.terminal
		
def build_dictionary():
	dictionary = Node()
	words_file = open('words.txt', 'r')
	
	try:
		for word in words_file:
			dictionary.insert(word.lower().rstrip()) # Need to use rstrip to remove trailing newline (\n) character
			
		return dictionary
	finally:
		words_file.close()
		
def find_anagrams(letters, dictionary, length):
	if letters.find('*') > 0:
		for letter in ascii_lowercase:
			for anagram in find_anagrams(letters.replace('*', letter, 1), dictionary, length):
				yield anagram
	else:
		for permutation in permutations(letters, length):
			word = ''.join(permutation)
		
			if dictionary.find(word):
				yield word
	
def main():
	t = time()
	dictionary = build_dictionary()
	print 'Loaded dictionary in {0} seconds'.format(time() - t)

	while True:
		letters = raw_input('Enter in your letters (use * for wildcards): ').lower()

		count = 0
		t = time()
		
		for i in range(2, len(letters) + 1):
			print i, 'letter words:'
		
			for anagram in find_anagrams(letters, dictionary, i):
				print anagram,
				count += 1
				
			print '\n'
				
		print 'Found {0} anagrams in {1} seconds'.format(count, time() - t)	
	
if __name__ == '__main__':
	main()