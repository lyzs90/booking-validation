# coding=utf-8
#!/usr/bin/env python3

"""
*****************
Utils module
*****************

This module contains helper functions to take in a sequence of bookings for a single car and outputs a single permutation of the input that minimises the total number of relocations within the sequence.

Given an input JSON file containing the booking sequence:
::

    [
        { "id": 1, "start": 23, "end": 42 },

        { "id": 2, "start": 77, "end": 45},

        { "id": 3, "start": 42, "end": 77 },

        . . .
    ]

The expected output is a JSON file consisting of an array of booking IDs of the reordered sequence:
::

    [1, 3, 2]

"""

import json
import random
from collections import deque


def get_list(file):
    """
    This function takes in a json file and deserialises to a Python list
    
    :param file: input file
    :type json: JSON file
    :return: returns a Python list
    :rtype: list
    """
    with open(file) as f:
        d = json.load(f)
        return d


def reorder_sequence(sequence, method, **kwargs):
    """
    This function takes in a list and reorders it using one of the available methods
    
	:param sequence: input booking sequence
    :type list: list containing the booking sequence
    :param method: method for sorting a list
    :type function: sorting function
    :param kwargs: arguments for the sorting function
    :return: returns a function with the supplied arguments
    :rtype: function
    """
    return method(sequence, kwargs)


def recursive_sort(sequence, kwargs):
    """
    Method for recursively sorting a booking sequence. Assumes that time of booking and distance between 
    locations do not matter. Inspired by the blockchain, start with a single record and then maintain a 
    continuously-growing list of ordered records. For each iteration, a forward pass appends a match to the
    block and a backward pass prepends a match to the end of the block.
    
    Forward pass:
    1. Cache the start and end location of the block
    2. Check the remaining bookings for a start location that matches the block's end location.
    3. If present, add this booking to end of the block and go to step 1.
    
    Backward pass:
    1. Cache the start and end location of the block
    2. Check the remaning bookings for an end location that matches the block's start location.
    3. If present, add this booking to the start of thr block and go to step 1.
    
    :param sequence: input booking sequence
    :type list: list containing the booking sequence
    :param iterations: number of iterations to run recursive sort. trade off runtime for accuracy.
    :type integer: number of iterations
    :return: returns a Python list containing the best sorted sequence
    :rtype: list
    """
    iterations = kwargs['iterations']  # unpack argument list
    relocations = len(sequence) + 1  # arbitrary no. gt number of bookings in sequence
    best_sequence = []
    
    for iteration in range(0, iterations):
        bookings = deque(sequence)  # use deque for performance boost
        first_booking = random.choice(bookings)
        block = deque([first_booking])
        if first_booking in bookings:
            bookings.remove(first_booking)

        for j in range(0, len(bookings)):
            # do forward pass
            try:
                match_forward = forward_pass(block, bookings)
                choice = random.choice(match_forward)  # note: returns the index of the match, not the bookings
                block.append(bookings[match_forward[choice]])  # append a random match
                del bookings[match_forward[choice]]  # remove match from remaining bookings
            except:
                pass

            # do backward pass
            try:
                match_backward = backward_pass(block, bookings)
                choice = random.choice(match_backward)  # note: returns the index of the match, not the bookings
                block.appendleft(bookings[match_backward[choice]])  # prepend a random match
                del bookings[match_backward[choice]]  # remove match from remaining bookings
            except:
                pass

        if len([item['id'] for item in bookings]) < relocations:
            remainder = [item['id'] for item in bookings]
            relocations = len(remainder)
            best_sequence = [index['id'] for index in block]

    print("Best Sequence: {}, Relocations: {}, Remainder: {}".format(best_sequence, relocations, remainder))
    
    return best_sequence


def forward_pass(block, remaining_bookings):
	"""
    This function performs the forward pass
    
    :param block: current block of ordered bookings
    :type deque: collections.deque
    :param remaining_bookings: bookings that have yet to be sorted
    :type deque: collections.deque
	:return: returns the indices of the matched bookings
	:rtype: list
    """
	match = []
	for index, item in enumerate(remaining_bookings):
		if item['start'] == block[-1]['end']:
			match.append(index)
	return match


def backward_pass(block, remaining_bookings):
	"""
    This function performs the backward pass
    
    :param block: current block of ordered bookings
    :type deque: collections.deque
    :param remaining_bookings: bookings that have yet to be sorted
    :type deque: collections.deque
	:return: returns the indices of the matched bookings
	:rtype: list
    """
	match = []
	for index, item in enumerate(remaining_bookings):
		if item['end'] == block[0]['start']:
			match.append(index)
	return match


def export_list(sequence, outfile):
    """
    This function serialises a Python list to JSON
    
    :param sequence: list to be exported
    :type list: Python list
    :param outfile: output file name
    :type json: json file
    """
    with open(outfile, 'w') as f:
        json.dump(sequence, f)