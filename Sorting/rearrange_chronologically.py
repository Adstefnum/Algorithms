def rearrange_chronologically(entry):

	sorted(entry,key = min(ascii([e[0] for e in entry])))
	'''
The idea is to reorder by ascii values then for each
entry with same ascii value in the same position rerun it on that smaller 
subset starting now from their 2nd entry and keep on going
till all positions of every entry are distinctly chronologically
rearranged
	'''