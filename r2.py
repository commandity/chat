def read_file(file_name):
	lines = []
	with open(file_name, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			for msg in s[2:]: 
				allen_word_count =  allen_word_count + len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			for msg in s[2:]: 
				viki_word_count =  viki_word_count + len(msg)

	print('Allen speak', allen_word_count, 'send', allen_sticker_count, 'sticker', allen_image_count, 'image')
	print('Viki speak', viki_word_count, 'send', viki_sticker_count, 'sticker', viki_image_count, 'image')


# def write_file(file_name, lines):
# 	with open(file_name, 'w') as f:
# 		for line in lines:
# 			f.write(line + '\n')


def main(file_name1):
	lines = read_file(file_name1)
	lines = convert(lines)
	# write_file(file_name2, lines)
	

main('viki.txt')