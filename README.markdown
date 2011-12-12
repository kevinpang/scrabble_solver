# Description

A simple anagram finder.

# Sample Usage

Without wildcards

	$ python scrabble_solver.py
	Loaded dictionary in 4.6802380085 seconds
	Enter in your letters (use * for wildcards): abc
	2 letter words:
	ab ba ca 

	3 letter words:
	bac cab 

	Found 5 anagrams in 0.000149965286255 seconds
	
With wildcards

	$ python scrabble_solver.py
	Loaded dictionary in 4.63677501678 seconds
	Enter in your letters (use * for wildcards): ab*
	2 letter words:
	ab aa ... ba za 

	3 letter words:
	aba baa ... aby bay 

	Found 135 anagrams in 0.00129699707031 seconds
	