from tkinter import *
import db_file

root = Tk()

frm1 = Frame(root)
frm1.grid(row=0, column=0)
frm2 = Frame(root)
frm2.grid(row=1, column=0)
frm3 = Frame(root)
frm3.grid(row=2, column=0)

nameLbl = Label(frm1, text="이름: ")
nameLbl.grid(row=0, column=0, sticky='E')
nameEntry = Entry(frm1, bg="light green")
nameEntry.grid(row=0, column=1)

scoreLbl = Label(frm1, text="점수: ")
scoreLbl.grid(row=0, column=2, sticky='E')
scoreEntry = Entry(frm1, width=10, bg="light green")
scoreEntry.grid(row=0, column=3, sticky='W')

numLbl = Label(frm1, text="번호: ")
numLbl.grid(row=1, column=2, sticky='E')
numEntry = Entry(frm1, width=7, bg="light green")
numEntry.grid(row=1, column=3, sticky='W')

fileLbl1 = Label(frm1, text="파일이름: ")
fileLbl1.grid(row=2, column=2, sticky='E')
fileEntry1 = Entry(frm1, bg="light blue")
fileEntry1.grid(row=2, column=3)

fileLbl2 = Label(frm1, text="파일이름: ")
fileLbl2.grid(row=3, column=2, sticky='E')
fileEntry2 = Entry(frm1, bg="light blue")
fileEntry2.grid(row=3, column=3)

txt = Text(frm3, width=60, height=10, bg="light yellow")
txt.grid(row=0, column=0)
stateTxt = Text(frm3, width=60, height=1, bg="pink")
stateTxt.grid(row=1, column=0)

data = [[0 for col in range(4)] for row in range(10)]
for i in range(10):
	data[i][3] = False

def click1(key):
	global data
	stateTxt.delete(1.0, END)
	if key == '추가':
		if nameEntry.get() == "":
			result = "이름을 확인하여 주세요"
		elif scoreEntry.get() == "":
			result = "점수를 확인하여 주세요"
		elif numEntry.get() == "":
			result = "번호를 확인하여 주세요"
		elif name_check(data, nameEntry.get()) == True:
			result = "이름 중복 입니다"
		elif num_check(data, numEntry.get()) == True:
			result = "번호 중복 입니다"
		else:
			for i in range(10):
				if data[i][3] == False:
					data[i][0] = numEntry.get()
					data[i][1] = nameEntry.get()
					data[i][2] = scoreEntry.get()
					data[i][3] = True
					break
			print_data(data)
			result = "성공적으로 추가하였습니다"
			nameEntry.delete(0, END)
			scoreEntry.delete(0, END)
			numEntry.delete(0, END)
		stateTxt.insert(END, result)
	elif key == "삭제":
		if numEntry.get() == "":
			result = "번호를 확인하여 주세요"
		elif num_check(data, numEntry.get()) == False:
			result = "삭제에 실패하였습니다"
		else:
			for i in range(10):
				if data[i][0] == numEntry.get():
					data[i][0] = ""
					data[i][1] = ""
					data[i][2] = ""
					data[i][3] = False
					break
			print_data(data)
			result = "성공적으로 삭제하였습니다"
			numEntry.delete(0, END)
		stateTxt.insert(END, result)
	elif key == "저장":
		if fileEntry1.get() == "":
			result = "파일 저장에 실패하였습니다"
		else:
			filename = fileEntry1.get() + ".pkl"
			db_file.file_save(filename, data)
			result = "성공적으로 저장였습니다 (파일이름: " + fileEntry1.get() + ")"
			fileEntry1.delete(0, END)
		stateTxt.insert(END, result)
	elif key == "열기":
		if fileEntry2.get() == "":
			result = "파일 불러오기에 실패하였습니다"
		else:
			filename = fileEntry2.get() + ".pkl"
			data = db_file.file_open(filename)
			result = "성공적으로 파일을 읽었습니다 (파일이름: " + fileEntry2.get() + ")"
			fileEntry2.delete(0, END)
			print_data(data)
		stateTxt.insert(END, result)

button_list1 = ["추가", "삭제", "저장", "열기"]

r = 0
for lst in button_list1:
	def cmd(x = lst):
		click1(x)
	Button(frm1, text=lst, width=7, command=cmd).grid(row=r, column=4)
	r = r + 1

def click2(key):
	global data
	stateTxt.delete(1.0, END)
	if key == "번호순":
		num_sort(data)
	elif key == "이름순":
		name_sort(data)
	elif key == "점수내림차순":
		score_sort_des(data)
	elif key == "점수오름차순":
		score_sort_asc(data)

button_list2 = ["번호순", "이름순", "점수내림차순", "점수오름차순"]
button_list2_width = [5, 5, 20, 20]

c = 1
for lst in button_list2:
	def cmd(x = lst):
		click2(x)
	Button(frm2, text=lst, width=button_list2_width[c-1], command=cmd).grid(row=0, column=c)
	c = c + 1

def print_data(data):
	txt.delete(1.0, END)
	for i in range(10):
		if data[i][3] == True:
			txt.insert(END, data[i][0] + "	" + data[i][1] + "		" + data[i][2] + "\n")

def num_check(data, num):
	for i in range(10):
		if data[i][0] == num:
			return True
	return False

def name_check(data, name):
	for i in range(10):
		if data[i][1] == name:
			return True
	return False

def num_sort(data):
	txt.delete(1.0, END)
	data.sort(key=lambda x: int(x[0]))
	print_data(data)

def name_sort(data):
	txt.delete(1.0, END)
	data.sort(key=lambda x: str(x[1]))
	print_data(data)

def score_sort_asc(data):
	txt.delete(1.0, END)
	data.sort(key=lambda x: float(x[2]), reverse=True)
	print_data(data)

def score_sort_des(data):
	txt.delete(1.0, END)
	data.sort(key=lambda x: float(x[2]))
	print_data(data)

root.mainloop()