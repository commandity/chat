def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(file_name, lines):
	with open(file_name, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main(file_name1, file_name2):
	lines = read_file(file_name1)
	lines = convert(lines)
	write_file(file_name2, lines)
	
main('input.txt', 'output.txt')