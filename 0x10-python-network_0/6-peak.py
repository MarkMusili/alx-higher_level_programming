#!usr/bin/python3
"""This file defines a function that
Calculates the peak of an unsorted list"""


def find_peak(list_of_integers):
	"""This function find the peak"""
	if list_of_integers:
		return max(list_of_integers)
	else:
		return None
