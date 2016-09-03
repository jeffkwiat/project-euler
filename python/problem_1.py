#!/bin/python3

def problem_1(max):
	results = []
	for number in range(1, max):
		if number % 3 == 0 or number % 5 == 0:
			results.append(number)
	print(sum(results))
		
if __name__ == '__main__':
	problem_1(1000)