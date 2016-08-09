import os

def file_save(filename, data):
	path = os.getcwd() + '\\' + filename
	f = open(path, 'w')
	for i in range(10):
		if data[i][3] == True:
			sdata = data[i][0] + "	" + data[i][1] + "	" + data[i][2] + "\n"
			f.write(sdata)
	f.close()

def file_open(filename):
	d = [[0 for col in range(4)] for row in range(10)]
	for i in range(10):
		d[i][3] = False

	path = os.getcwd() + '\\' + filename
	f = open(path, 'r')
	i = 0
	while True:
		line = f.readline()
		if not line:
			break
		d[i][0] = line.split('	')[0]
		d[i][1] = line.split('	')[1]
		s = line.split('	')[2]
		d[i][2] = s[:len(s)-1]
		d[i][3] = True
		i = i + 1

	return d