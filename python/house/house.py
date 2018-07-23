parts = [('lay in', 'the house that Jack built.'),
		 ('ate', 'the malt'),
		 ('killed', 'the rat'),
		 ('worried', 'the cat'),
		 ('tossed', 'the dog'),
		 ('milked', 'the cow with the crumpled horn'),
		 ('kissed', 'the maiden all forlorn'),
		 ('married', 'the man all tattered and torn'),
		 ('woke', 'the priest all shaven and shorn'),
		 ('kept', 'the rooster that crowed in the morn'),
		 ('belonged to', 'the farmer sowing his corn'),
		 ('', 'the horse and the hound and the horn')]

def recite(start_verse, end_verse):
	result = []
	for num in range(start_verse-1, end_verse):
		v = ['This is {}'.format(parts[num][1])]
		v.extend(['that {0} {1}'.format(*parts[i]) for i in range(num - 1, -1, -1)])
		result.append(' '.join(v))
	return result
