from itertools import pairwise


test_data = [
	[7,6,4,2,1],
	[1,2,7,8,9],
	[9,7,6,2,1],
	[1,3,2,4,5],
	[8,6,4,4,1],
	[1,3,6,7,9]
	]


def remove_list_element(index, list):
	newlist = [x for x in list]
	del newlist[index]
	return newlist


def input_parser(file):
	with open(file) as file:
		ints = []
		
		for line in file:
			strings = line.strip().split(' ')
			converted = []
			
			for element in strings:
				converted.append(int(element))
			
			ints.append(converted)
			
		return ints
		
		
def compare_list_elements(list):
	comparisonsummary = []
	stable = None
	
	for element, pair in pairwise(list):
		comparisonsummary.append(element - pair)
	
	if any(x==0 for x in comparisonsummary):
		stable = False
	elif all((1 <= x <= 3)for x in comparisonsummary):
		stable = True
	elif all((-1 >= x >= -3) for x in comparisonsummary):
		stable = True
	else:
		stable = False
	
	return stable
	

def problem_dampener(unsafereport):
	unsafetuple = tuple(unsafereport)
	brute_list = []
	test_cases = []
		
	for i in range(0, (len(unsafetuple))):
		brute_list.append(remove_list_element(i, unsafetuple))
		
	for list in brute_list:
		test_cases.append(compare_list_elements(list))
			
	if True in test_cases:
		return True
	else:
		return False


detailed_summary = []
unsafe_reports = []
stability_report = {True: 0, False: 0}
parsed_input = input_parser('input.txt')

for list in parsed_input:
#	detailed_summary.append([list, compare_list_elements(list)])
	comparison = compare_list_elements(list)
	stability_report[comparison] += 1
	if comparison == False:
		unsafe_reports.append(list)

print(stability_report)

for list in unsafe_reports:
	safe = problem_dampener(list)
	
	if safe == True:
		stability_report[True] += 1
		stability_report[False] -= 1

#print(detailed_summary)
#print(unsafe_reports)
print(stability_report)

