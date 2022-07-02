# Bubble Sort
# Simplest sorting algorithm


def swap_elements(array, index_1, index_2):
	# Swaps elements in array
	array[index_1], array[index_2] = array[index_2], array[index_1]
	
	return None



def single_pass_adjacent_swapped(array):
	# On a single pass through the list, switch adjacent elements which are out of order.
	# Returns boolean:
	#	True: change was made (in which case we must pass through again)
	#	False: no change was made, the list is ordered
	#
	#	This sorter is stable

	changes_made = False # This is the flag to keep track of whether a change was made on a pass
	for i in range(0, len(array)-1): # Range insures we do not go out of range on the list
		if array[i] > array[i+1]:
			swap_elements(array,i,i+1)
			if not changes_made:
				changes_made = True

	return changes_made



def bubble_sort(array):
	# Make a copy of array so original list is not altered.
	# While single_pass_adjacent_swapped continues to be true, must check to see whether elements
	# 	continue to be out of order.
	# When single_pass_adjacent_swapped returns False then a pass has not required a swap, and the list
	# 	is sorted.

	copy_of_array = [element for element in array]
	while single_pass_adjacent_swapped(copy_of_array):
		pass

	return copy_of_array
