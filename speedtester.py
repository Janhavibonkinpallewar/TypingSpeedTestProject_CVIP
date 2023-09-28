from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()

window.geometry("500x500")

x = 0

# defining the function for the test
def SpeedTester():
	global x

	if x == 0:
		window.destroy()
		x = x+1

	# defining function for results of test
	def check_result():
		if entry.get() == words[word]:

			# here start time is when the window
			# is opened and end time is when
			# window is destroyed
			end = timer()

			# we deduct the start time from end
			# time and calculate results using
			# timeit function
			print(end-start)
		else:
			print("Wrong Input")

	words = ['Internships', 'Programming', 'Software',
			'Engineering', 'python', 'LearningandGrowing']

	#  words for testing the speed
	word = random.randint(0, (len(words)-1))

	# start timer 
	start = timer()
	windows = Tk()
	windows.geometry("450x200")

	# use label method of tkinter for labeling in window
	x2 = Label(windows, text=words[word], font="times 20")

	# place of labeling in window
	x2.place(x=150, y=10)
	x3 = Label(windows, text="Type given Word", font="times 20")
	x3.place(x=10, y=50)

	entry = Entry(windows)
	entry.place(x=250, y=50)

	# buttons 
	b2 = Button(windows, text="SUBMIT",
				command=check_result, width=16, bg='white')
	b2.place(x=150, y=100)

	b3 = Button(windows, text="EXIT",
				command=SpeedTester, width=16, bg='white')
	b3.place(x=250, y=100)
	windows.mainloop()


x1 = Label(window, text="TYPING SPEED TESTER", font="times 17")
x1.place(x=10, y=50)

b1 = Button(window, text="START", command=SpeedTester, width=12, bg='grey')
b1.place(x=150, y=100)

window.mainloop()
