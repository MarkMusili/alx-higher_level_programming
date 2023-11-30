#!usr/bin/python3
"""This file defines a function that
Calculates the peak of an unsorted list"""


def find_peak(list_of_integers):
	"""
	This function find the peak
	Args:
		list_of_intergers (list): list of unsorted integers
	Return:
		Returns the peak number or None
	"""
	if list_of_integers:
		return max(list_of_integers)
	else:
		return None
