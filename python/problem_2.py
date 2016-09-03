#!/bin/python3

def problem_2(number_terms):
	results = []
	start = 0
	for number in range(1, number_terms + 1):
		results.append(number)
	print(sum(results))
		
if __name__ == '__main__':
	problem_2(10)