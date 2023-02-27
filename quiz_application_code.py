from tkinter import *
import tkinter as tk
from tkinter import messagebox
'''
In this project we are using tkinter library for graphical user interface to make our project more user friendly
'''
#here root is the window of tkinter which is given a title with defined size
root= tk.Tk()
root.geometry("500x550")
root.title("Quiz application")
root.configure()
root.resizable(False,False)
#following are the frames in which different tasks are performed, these frames are defined by their names
f1_introductory=tk.Frame(root)
f2_admin=tk.Frame(root)
f3_adminopt=tk.Frame(root)
f6_studentlgn=tk.Frame(root)
f7_choice=tk.Frame(root)
f8_scieneoptd=tk.Frame(root)
f9_science_2=tk.Frame(root)
f10_gk1=tk.Frame(root)
f11_gk_2=tk.Frame(root)
f12_adminview=tk.Frame(root)
f13_addingQ=tk.Frame(root)
f14resuult=tk.Frame(root)
f15remove=tk.Frame(root)
f16sciview=tk.Frame(root)
f16gkview=tk.Frame(root)


#THIS IS A INTRODUCTORY FRAME IN WHICH USER WILL ASKED TO ENTER AS ADMIN OR STUDENT
introductionpage=tk.Label(f1_introductory, text="WELCOME TO THE QUIZ",font="bold 15",bg="white")
introductionpage.pack(fill=BOTH,pady=20)
#BELOW FUCNTION INDICATE IF A USER SELECT STUDENT THEN THE STUDENT INTERFACE WILL OPEN
def f1to6():
    f1_introductory.pack_forget()
    f6_studentlgn.pack()
student_setup=tk.Button(f1_introductory, text=" STUDENT  ", bg="grey",font="bold 40", command=f1to6)
student_setup.pack(side=BOTTOM,pady=14,fill=X)
#BELOW FUCNTION INDICATE IF A USER SELECT STUDENT THEN THE ADMIN INTERFACE WILL OPEN
def f1to2():
    f1_introductory.pack_forget()
    f2_admin.pack()
administrator=tk.Button(f1_introductory, text="ADMINISTRATOR ", bg="grey",padx=500,font="bold 40",command=f1to2)
administrator.pack(side=BOTTOM,fill=X,pady=14)


#for 2nd windows of administrator
def login():
    name = administratorname_entry.get()
    password = administratorpassword_stored.get()
    if name == "" and password == "":
        messagebox.showerror("warning","please enter user id and password")
    elif name != "" and password == "":
        messagebox.showerror("warning", "please insert password")
    elif name == "" and password != "":
        messagebox.showerror("warning", "enter user ID")
    elif name =="admin" and password=="admin":
        f2_admin.pack_forget()
        f3_adminopt.pack()
    else:
        messagebox.showerror("warning", "please enter correct password and user id")

#HERE LABEL IS A KEYWORD WHICH PRINT THE TEXT IN THE WINDOW OR FRAME
#ENTRY IS ALSO A FUNCTION USED TO INPUT DATA FROM THE USER
#PACK_FORGET CLOSES THE CURRENT FRAME AND OPEN THE DESIRE FRAME
#WE HAVE USED BUTTONS FOR THE COMMANDS AND RADIO BUTTON FOR SELECTING MCQS
administratorname = tk.Label(f2_admin, text="User ID", font="times 15 bold")
administratorname.pack(fill=X,pady=5)
administratorname_entry = tk.Entry(f2_admin, bg="white", font="times 15 bold")
administratorname_entry.pack(pady=5)
administratorpassword = tk.Label(f2_admin, text="Password", font="times 15 bold")
administratorpassword.pack(fill=X,pady=5)
administratorpassword_stored = tk.Entry(f2_admin, bg="white", font="times 15 bold",show="*")
administratorpassword_stored.pack(pady=5)
Label(f2_admin,text=" ").pack(pady=5)
loginbutton = tk.Button(f2_admin, text=" login", bg="grey", font="times 20 bold", command=login)
loginbutton.pack(fill=X,pady=5)
#BELOW FUNCTION IS USED TO JUMP TO FIRST WINDOW
def f2to1():
    f2_admin.pack_forget()
    f1_introductory.pack()
nextbutton=tk.Button(f2_admin, text="back ", bg="white", font="times 10 bold", command=f2to1)
nextbutton.pack(fill=X,pady=5)

#WHEN THE ADMIN INSERT CORRECT USERNAME AND PASSWORD HE WILL ASK TO SELECT WHAT HE WANT TO EDIT DELETE OR VIEW
Label(f3_adminopt, text="Hey Admin!!! ",font="bold 30").pack(anchor=W,pady=10)
def f3to12():
    f3_adminopt.pack_forget()
    f12_adminview.pack()
text2=tk.Label(f12_adminview, text=" Questions answer review",font="bold 30")
text2.pack(pady=10)
def backf12():
    f12_adminview.pack_forget()
    f3_adminopt.pack()

questionbank=tk.Button(f3_adminopt, text="View question bank",bg="grey",font="bold 30" ,pady=5,command=f3to12)
questionbank.pack(fill=X,pady=15)

def f16sci():
    f12_adminview.pack_forget()
    f16sciview.pack()

scienceVIEWbutton=tk.Button(f12_adminview, text="science",bg="grey",font="bold 30", command=f16sci)
scienceVIEWbutton.pack(fill=X,pady=12)
def f16gk():
    f12_adminview.pack_forget()
    f16gkview.pack()
GKVIEWbutton=tk.Button(f12_adminview, text="GENERAL KNOWLEGDE",bg="grey",font="bold 30", command=f16gk)
GKVIEWbutton.pack(fill=X,pady=12)
quitbutton=tk.Button(f12_adminview, text="BACK",bg="white", font="times 10 bold", command=backf12)
quitbutton.pack()

#viewing question in science
#IN ORDER TO VIEW QUESTION WE HAVE USED SCROLL BAR WHICH ENABLE THE FRAME TO MOVE UP AND DOWN.
def backviewSCIf16():
    f16sciview.pack_forget()
    f12_adminview.pack()
sciscroll=Scrollbar(f16sciview)
sciscroll.pack(side=RIGHT,fill=Y)
btnsci=Listbox(f16sciview,width=1000,height=25,font="16",yscrollcommand=sciscroll.set)
file=open("data_file.txt", "r")
file=open("data_file.txt", "r")
#FROM FILE, DATA IS READ COMPLETELY AND STORE IN A LIST AS EACH LINE HAS DIFFERENT INDEX . THEN USING SPLIT FUCNTION WE STORE THE EACH LINE IN A NESTED LIST USING INDEXING AND SPLITTING BY COMMAS
sciread=file.readlines()
for k in range(len(sciread)):
    S=sciread[k]
    science_list=S.split(",")
    if science_list[0]== "SCI":
        btnsci.insert(END, science_list[1]) #THIS WILL GIVE THE QUESTIONS
        for i in range(2,5):
            btnsci.insert(END, science_list[i]) #THIS WILL GIVE THE MCQS
        btnsci.insert(END, science_list[5], " ") #IT IS THE INDE OF ANSWER
btnsci.pack(side=TOP,fill=Y)
sciscroll.config(command=btnsci.yview)
backbtninsciview=tk.Button(f16sciview,text="back",command=backviewSCIf16)
backbtninsciview.pack(pady=3)

##viewing question in general knowledge

def backviewGKf16():
    f16gkview.pack_forget()
    f12_adminview.pack()

gkscroll=Scrollbar(f16gkview)
gkscroll.pack(side=RIGHT,fill=Y)
btngk=Listbox(f16gkview,width=1000,height=25,font="16",yscrollcommand=gkscroll.set)
#SEEK FUNCTION IS USED TO READ THE FILE FROM THE 0 POINT I.E STARTING POINT
file.seek(0)
gkread=file.readlines()
#THEN SAME THING WILL HAPPEN AS IN GK
for k in range(len(gkread)):
    G=gkread[k]
    gk_list=G.split(",")
    if gk_list[0]== "GK":
        btngk.insert(END, gk_list[1])
        for i in range(2,5):
            btngk.insert(END, gk_list[i])
        btngk.insert(END, gk_list[5], " ")
btngk.pack(side=TOP,fill=Y)
gkscroll.config(command=btngk.yview)
backbtningkview=tk.Button(f16gkview,text="back",bg="grey",command=backviewGKf16)
backbtningkview.pack(pady=5)


def f3to13():
    f3_adminopt.pack_forget() #THIS WILL CLOSE THE FRAME OF ADMIN SITE AND OPEN ADDING QUESTION
    f13_addingQ.pack()

text1=tk.Label(f13_addingQ, text="adding question",bg="white",font="bold 20")
text1.pack()


addquestion=tk.Button(f3_adminopt, text=" add questions", bg="grey",font="bold 30",command=f3to13)
addquestion.pack(fill=X,pady=10)


#APPENDING QUESTIONS

def appending():
    option_aget=option_a.get() #IT STORES THE STRING OF OPTION A AT INDEX 2
    option_bget=option_b.get() #IT STORES THE STRING OF OPTION B AT INDEX 3
    option_cget=option_c.get() #IT STORES THE STRING OF OPTION C AT INDEX 4
    questionget=questions.get() #IT STORES THE STRING OF QUESTION AT INDEX 1
    categoryget=categories.get() #IT GET THE CATEGORY NAME AT INDEX 0
    correct_answerget=correct_answer.get() #IT STORES THE CORRECT ANSWER AT INDEX 5
    # "'adding questions in the my_file'"
    file=open("data_file.txt", "a+") #FILE IS OPEN IN APPEND+ MODE WHICH INDICATE IT PERFORM ALL THE FUNCTION OF APPENDING
    file.write("\n") #IN APPEND MODE CURSOR IS IN AT THE LAST LINE AND AT LAST CHARACTER SO IT'S NECCESSARY TO PRINT NEXT LINE
    file.write(categoryget.upper()) #AFTER ENTER FIRST IT WRITE THE CATEGORY IN THE FILE
    file.write(",") #THEN COMMAS ARE USE TO SEPERATE EACH DIFFERECT COMPONENTS OF MCQS
    file.write(questionget) #SIMILARLY QUESTIONS, OPTIONS AND ANSWER WILL BE INSERTED
    file.write(",")
    file.write(option_aget)
    file.write(",")
    file.write(option_bget)
    file.write(",")
    file.write(option_cget)
    file.write(",")
    file.write(correct_answerget)
    file.close()
    messagebox.showinfo("QUESTION ADDED","PLEASE RERUN THE APPLICATION TO VIEW QUESTION")
    f13_addingQ.quit()
Label(f13_addingQ,text="NOTE: INSTEAD OF USING commas(,) PLEASE USE apostrophe(')").pack()

Label(f13_addingQ, text="category SCI or GK ",font="bold 20",bg="white").pack(anchor=N,pady=15)
categories=tk.Entry(f13_addingQ, bg="white", width=15, font="times 15 bold")
categories.pack(pady=5)
Label(f13_addingQ, text="insert question",font="times 15 bold",bg="white").pack(anchor=N)
questions=tk.Entry(f13_addingQ, bg="white", width=200, font="times 15 bold")
questions.pack(pady=5)
Label(f13_addingQ, text="insert OPTION A",font="times 15 bold",bg="white").pack(anchor=N)
option_a=tk.Entry(f13_addingQ, bg="white", font="times 15 bold")
option_a.pack(anchor=N,pady=5)
Label(f13_addingQ, text="insert OPTION B",font="times 15 bold",bg="white").pack(anchor=N)
option_b=tk.Entry(f13_addingQ, bg="white", font="times 15 bold")
option_b.pack(pady=5)
Label(f13_addingQ, text="insert OPTION C",font="times 15 bold",bg="white").pack(anchor=N)
option_c=tk.Entry(f13_addingQ, bg="white", font="times 15 bold")
option_c.pack(pady=5)
Label(f13_addingQ, text="CORRECT ANSWER (mcq index)",font="times 15 bold",bg="white").pack(anchor=N)
correct_answer=tk.Entry(f13_addingQ, bg="white", font="times 15 bold")
correct_answer.pack(pady=5)

def done_quit():
    f13_addingQ.pack_forget()
    f3_adminopt.pack()
backbuttonf13=tk.Button(f13_addingQ, text="back",bg="grey" ,font="bold",command=done_quit)
backbuttonf13.pack()



f15donebuttongk=tk.Button(f13_addingQ, text="done", font="bold",command=appending)
f15donebuttongk.pack()

#remove/deleting questions
file=open("data_file.txt", "r")
read = file.readlines()
def remove():
    f3_adminopt.pack_forget()
    f15remove.pack()
    overview=Tk()
    overview.geometry("500x400")
    overview.title("QUESTION BANK")
#WE HAVE USED SCROLLBAR AND LISTBOX IN ORDER TO SHOW THE ADMIN ABOUT THE INDEX OF A QUESTION THEN HE WILL BE ABLE TO DELETE WHICH QUESTION HE WANTS TO DELETE
    overview_scroll = Scrollbar(overview)
    overview_scroll.pack(side=RIGHT, fill=Y)
    overview_list = Listbox(overview, width=1000, height=35, font="16", yscrollcommand=overview_scroll.set)
    for k in range(len(read)):
        readsplit = read[k]
        questionsscroll=readsplit.split(",")
        # overview_list.insert(END,k+1)
        overview_list.insert(END,k ,questionsscroll[1])
        for i in range(2,5):
            overview_list.insert(END,questionsscroll[i])
        overview_list.insert(END,"  ")

    overview_list.pack(side=TOP, fill=Y)
    overview_scroll.config(command=overview_list.yview)
    overview.mainloop()
removebutton=Button(f3_adminopt, text="remove/delete",bg="grey",font="bold 30",command=remove)
removebutton.pack(fill=X,pady=10)
file.close()

Label(f15remove,text="remove question").pack(pady=10)
Label(f15remove,text="which question do you want to delete? (write number from the given list)",font="bold").pack(pady=10)


remove_entry=tk.Entry(f15remove,width=100)
remove_entry.pack(pady=10)


def entryin_f15remove():
    file = open("data_file.txt", "r+")#OPEN A FILE IN A READ+ MODE
    lines = file.readlines() #Data stored in a list
    removequestion=remove_entry.get() #value in string form from the entry box is assigned to variable then type casted to
    lines.pop(int(removequestion)) #by using list comprehension .pop command delete the element of list by index number
    file = open("data_file.txt", "w")
    # opens a file in w mode which means all the data written in file will be deleted then by using loop the data stored in lines(a list) which will be again written in file
    for k in range(len(lines)):
        file.write(lines[k])

    file.close()
    messagebox.showinfo("QUESTION DELETED","PLEASE RERUN THE APPLICATION TO VIEW QUESTION")
    f15remove.quit()
file.close()

doneremove=Button(f15remove,text="done",bg="white",command=entryin_f15remove)
doneremove.pack(pady=10)

def backentry():
    f15remove.pack_forget()
    f3_adminopt.pack()
back_entry=tk.Button(f15remove,text="BACK",bg="white", font="times 10 bold",command=backentry)
back_entry.pack()

def f3tof2closebutton():
    f3_adminopt.pack_forget()
    f2_admin.pack()
closebutton=tk.Button(f3_adminopt, text="close",bg="white", font="bold 10",command=f3tof2closebutton)
closebutton.pack(pady=5)

#for student's interface frame 6
#from now we work for the interface of student .In the start two options will be shown to student for selecting their interesting field for quiz
def student():
    studentnameget = studentname.get()
    rollnumberget = rollnumber.get()
    if studentnameget == "" and rollnumberget == "":
        messagebox.showerror("warning","please your name and roll number")
    elif studentnameget != "" and rollnumberget== "":
        messagebox.showerror("warning", "please enter your roll number")
    elif studentnameget == "" and rollnumberget != "":
        messagebox.showerror("warning", "enter name")
    elif studentnameget!="" and rollnumberget!="":
        #here f14result is a frame in which result name of student with roll number is printed
        tk.Label(f14resuult, text="RESULT", font="times 40 bold").pack()
        tk.Label(f14resuult, text="STUDENT NAME:--", font="times 10 bold").pack(anchor=W)
        tk.Label(f14resuult, text=studentnameget,font="times 20 bold").pack(anchor=W)
        tk.Label(f14resuult, text="ROLL NUMBER:--", font="times 10 bold").pack(anchor=W)
        tk.Label(f14resuult, text=rollnumberget,font="times 20 bold").pack(anchor=W)
        f6_studentlgn.pack_forget()
        f7_choice.pack()
        with open("student_record.txt", "a") as file1:   #to record data of student we create a new file to write the name roll number and score of selected domain
            file1.write("name"+":- "+ studentnameget+ ", "+ "roll number " + ":- "+rollnumberget+", ")
#STUDENT INFORMATION IS COLLECTED IN THE STUDENT PORTAL AND STORED IN RESULT FRAME
#WE HAVE USED ENTRY BOX TO COLLECT THE DATA OF STUDENT
Label(f6_studentlgn, text="STUDENT PORTAL", font="times 20 bold").pack(pady=15)
student1 = tk.Label(f6_studentlgn, text="Your name", font="times 15 bold")
student1.pack(pady=10)
studentname = tk.Entry(f6_studentlgn, bg="white", font="times 15 bold")
studentname.pack()
studentrollnumber = tk.Label(f6_studentlgn, text="Student roll number", font="times 15 bold")
studentrollnumber.pack()
rollnumber= tk.Entry(f6_studentlgn, bg="white", font="times 15 bold")
rollnumber.pack()

nextbutton=tk.Button(f6_studentlgn, text="Start quiz",font="times 15 bold",bg="grey" ,command=student)
nextbutton.pack(pady=5)
#THEN THE QUIZ PART WILL BE SHOWN AND FROM TWO DOMAINS STUDENT CAN SELECT ANY ONE
def f6to1():
    f6_studentlgn.pack_forget()
    f1_introductory.pack()
backbutton=tk.Button(f6_studentlgn, text="back",font="times 15 bold",bg="grey" ,command=f6to1)
backbutton.pack(pady=5)

def f7to8():
    f7_choice.pack_forget()
    f8_scieneoptd.pack()
Label(f7_choice, text="select any one",bg="white",font="bold 40").pack(pady=15)
nextbuttoninquiz1=tk.Button(f7_choice, text="Science",bg="grey",font="bold 30" ,command=f7to8)
nextbuttoninquiz1.pack(fill=X,pady=10)

def f7to10():
    f7_choice.pack_forget()
    f10_gk1.pack()
nextbuttoninquiz2=tk.Button(f7_choice, text="General knowledge",bg="grey",font="bold 30", command=f7to10)
nextbuttoninquiz2.pack(fill=X,pady=10)

def backf7():
    f7_choice.pack_forget()
    f6_studentlgn.pack()
backinf7=Button(f7_choice, text="back",font="bold",bg="white",command=backf7)
backinf7.pack()
selectedoption=tk.Label(f8_scieneoptd, text="you have selected science")
selectedoption.pack()
#from this point we are inserting data to science frame

#initizalizing options of science with "" because in tkinter radiobuttons required variable value of same question set of buttons.
optionSCI1,optionSCI2,optionSCI3,optionSCI4,optionSCI5,optionSCI6,optionSCI7,optionSCI8,optionSCI9,optionSCI10='','','','','','','','','',''
#then we have stored the above options in a list to assign a different option to variable
correctoption_index=[optionSCI1,optionSCI2,optionSCI3,optionSCI4,optionSCI5,optionSCI6,optionSCI7,optionSCI8,optionSCI9,optionSCI10]

file=open("data_file.txt", "r")
readscience=file.readlines()
l=[]
#using readlines function we have transfered our whole data of file into readscience variable then in extra we initialize the list with l
for i in range(len(readscience)):
    questioninsciece=readscience[i] #each index of readsciene  is then converted to string which can be separted by split function
    questioninsciecesplit=questioninsciece.split(",")
    if questioninsciecesplit[0]=="SCI": #if the 0 index of readscience is sci it append the nested list of whole set (consist of category Q,a,b,c,ANSWER) in a list l
        l.append(questioninsciecesplit)
#our quiz is mainly divided into two frames consist of 5,5 question in each part
for k in range(5):
    mcqs_question = tk.Label(f8_scieneoptd, text=l[k][1],font="bold")
    mcqs_question.pack(anchor=W)
    correctoption_index[k] = IntVar()
    for j in range(2, 5):
        givenoptionof_SCI = tk.Radiobutton(f8_scieneoptd, text=l[k][j], value=j - 1, variable=correctoption_index[k])
        #value in above line indicate different values are assign to radiobutton which can be used to correct our answer in a loop of counter
        givenoptionof_SCI.pack(anchor=W)
#here l is the list comprises of science data
def f8to9():
    f8_scieneoptd.pack_forget()
    f9_science_2.pack()
nextbuttoninscience=tk.Button(f8_scieneoptd, text="next", bg="white",font="bold",command=f8to9)
nextbuttoninscience.pack()

file.close()
#same happens with the general knowledge part
for k in range(5,10):
    mcqs_question = tk.Label(f9_science_2, text=l[k][1],font="bold")
    mcqs_question.pack(anchor=W)
    correctoption_index[k] = IntVar()
    for j in range(2, 5):
        givenoptionof_SCI = tk.Radiobutton(f9_science_2, text=l[k][j], value=(j - 1), variable=correctoption_index[k])
        givenoptionof_SCI.pack(anchor=W)

#below functions refer to print the resultof science quiz in the result frame and data inserted by student
def submitscience():
    messagebox._show("submit", "your quiz is submitted")
    score_sciene = 0 #initializing the student_record.txt of scince to zero
    for k in range(10):
        if correctoption_index[k].get() == int(l[k][5]):#it fetches the value of radio button assign to one set of questions ,if matche with index 5 it add one marks and same for the whole 10 questions
            score_sciene += 1
    tk.Label(f14resuult, text="You have scored in science",font="bold").pack()
    tk.Label(f14resuult, text=score_sciene,font="bold").pack()
    with open("student_record.txt", "a") as file1: #we open a separate file to write the score of student who selected domain of science
        file1.write("score"+":- "+str(score_sciene)+" in science"+"\n")
    f9_science_2.pack_forget()
    f14resuult.pack()
    if score_sciene>5:
        tk.Label(f14resuult,text="remarks:-- you have passed the test").pack(side=BOTTOM) #if the user's student_record.txt is greater than 5 ,he clears the test otherwise fail.
    else:
        tk.Label(f14resuult, text="remarks:-- better luck next time").pack(side=BOTTOM)

def f9to8():
    f9_science_2.pack_forget()
    f8_scieneoptd.pack()
backbuttoninscience=tk.Button(f9_science_2, text="previous page",font="bold 10",bg="white", command=f9to8)
backbuttoninscience.pack()
#by clicking submit button student an view his\her result
checkscoreinsciece=tk.Button(f9_science_2, text="submit your quiz",font="bold 10" ,bg="red",command=submitscience)
checkscoreinsciece.pack()

#working in general knowlegde
selectedoption_gk=tk.Label(f10_gk1, text="You have selected general knowlegde")
selectedoption_gk.pack()
def f10to11():
    f10_gk1.pack_forget()
    f11_gk_2.pack()
#from this point we are inserting data to general knowledge frame
#initizalizing options of science with "" because in tkinter radiobuttons required variable value of same question set of buttons.
optionGK1,optionGK2,optionGK3,optionGK4,optionGK5,optionGK6,optionGK7,optionGK8,optionGK9,optionGK10='','','','','','','','','',''
option=[optionGK1,optionGK2,optionGK3,optionGK4,optionGK5,optionGK6,optionGK7,optionGK8,optionGK9,optionGK10]
file=open("data_file.txt", "r") #opens the file in read mode
readGK=file.readlines() #save the data in a list
G=[]
for i in range(len(readscience)):
    questioninGK=readGK[i]
    questioninGKsplit=questioninGK.split(",")
    if questioninGKsplit[0]=="GK":
        G.append(questioninGKsplit) #append the question in THE LIST OF G
#five questions will be printed in frame of gk1
for k in range(5):
    tk.Label(f10_gk1, text=G[k][1],font="bold").pack(anchor=W)
    option[k] = IntVar()
    for j in range(2, 5):
        givenoptionof_GK = tk.Radiobutton(f10_gk1, text=G[k][j], value=j - 1, variable=option[k])
        # value in above line indicate different values are assign to radiobutton which can be used to correct our answer in a loop of counter
        givenoptionof_GK.pack(anchor=W)
nextbuttonin_gk=tk.Button(f10_gk1, text="next" ,bg="white",font="bold",command=f10to11)
nextbuttonin_gk.pack()
#remaining five questions will be printed in frame of gk2
for k in range(5,10):
    mcqs_question = tk.Label(f11_gk_2, text=G[k][1],font="bold")
    mcqs_question.pack(anchor=W)
    option[k] = IntVar()
    for j in range(2, 5):
        givenoptionof_GK = tk.Radiobutton(f11_gk_2, text=G[k][j], value=(j - 1), variable=option[k])
        givenoptionof_GK.pack(anchor=W)

#below is the function which shows the result of student who has selected the general knowledge part at the start
def submitgk():
    score_gk=0
    for k in range(10):
        if option[k].get() == int(G[k][5]):
            score_gk += 1
    messagebox.showinfo("submit", "your quiz is submitted")
    tk.Label(f14resuult, text="You have scored in general knowledge",font="bold").pack(anchor=W)
    tk.Label(f14resuult, text=score_gk,font="bold").pack()
    with open("student_record.txt", "a") as file1: #opens a file in order to write the score and selected domain in the separate file
        file1.write("score "+":- "+str(score_gk)+" in general knowledge"+"\n")
    if score_gk>5:
        tk.Label(f14resuult,text="remarks:-- you have passed the test").pack(side=BOTTOM)
    else:
        tk.Label(f14resuult, text="remarks:-- better luck next time").pack(side=BOTTOM)
    f11_gk_2.pack_forget()
    f14resuult.pack()
checkscorein_gk=tk.Button(f11_gk_2, text="submit your quiz",bg="red" ,command=submitgk)
checkscorein_gk.pack()


def f11tof10(): #this function bring the student to first page of general knowlegde during quiz
    f11_gk_2.pack_forget()
    f10_gk1.pack()
backbuttonin_gk=tk.Button(f11_gk_2, text="previous page",bg="white", command=f11tof10)
backbuttonin_gk.pack()

def resultframe(): #this function lead to introdcuctory frame
    f14resuult.pack_forget()
    f1_introductory.pack()
buttonresult=tk.Button(f14resuult,text="back to first page",bg="white",command=resultframe)
buttonresult.pack()
f1_introductory.pack()
root.mainloop()