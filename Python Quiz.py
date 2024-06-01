from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root=Tk()
root.title('Login page')
root.geometry('963x781')        #canvas aspect ratio
root.configure(bg='#222325')   #Background color
root.resizable(False,False)


def signin():   #funtion for checking password and username and going to next page
    username = user.get()       
    password = code.get()


    if username == 'admin' and password == '1234':
        root.destroy()
        screen = Tk()
        screen.title("app")
        screen.geometry('963x781')
        screen.config(bg = '#222325')
        screen.resizable(False,False)
#======================================================== DIFFICULT HEADING =========================================================#
        
        heading=Label(screen,text="Choose your Difficulty level",fg='white',bg='#222325',font=('Courier',26,'bold'))
        heading.place(x=175,y=55)


        frame=Frame(screen,width=1000,height=60,bg='#222325')  
        frame.place(x=0,y=100)

        heading=Label(frame,text="Based on your selected difficulty level,we will select an appropriate problem for\nyou to solve. ",fg='white',bg='#222325',font=('Bahnschrift SemiLight',12))
        heading.place(x=175,y=10)



#======================================================== MODERATE BODY =========================================================#
        def on_enter(event):
            frame2.config(bg='#2B2B2B')
            label2.config(bg='#2B2B2B')
            heading2.config(bg='#2B2B2B')
            abt3.config(bg='#2B2B2B')
            button2.config(bg='#80C454')

# Function to change frame color when mouse leaves
        def on_leave(event):
            frame2.config(bg='#222325')
            label2.config(bg='#222325')
            heading2.config(bg='#222325')
            abt3.config(bg='#222325')
            button2.config(bg='#2B2B2B')


        def Moderate_button():
            Mod=Toplevel(screen)
            Mod.title('Question')
            Mod.geometry('963x781')        #canvas aspect ratio
            Mod.configure(bg='#222325')   #Background color
            Mod.resizable(False,False)
            global heading2,i                #Heading2 questions 
            heading2 = None
            i = 0

            global questions,answers,correct_ans,user_score
            questions = ["What is the character used for single-line comments in Python?","What is the order of operations in Python called? ","What is the output of the expression 3 % 2 in Python?","Which of the following methods can be used to read the \nfirst line of a file in Python?","Which method can be used to remove whitespace from the \nbeginning and the end of a string?"]
            answers = [['@','&','#','none'],['PEMDAS','Parentheses','Exponents','bodmas'],['1.5','2','1','3'],['file.read()','file.readline()','file.readlines()','file.readfirstline()'],['strip()','trim()','remove()','cut()']]
            correct_ans = ['#','PEMDAS','1','file.readline()','strip()']
            global selected_ans
            selected_ans = None
            user_score=0



            container_frame = Frame(Mod,width = 850,height = 550,bg = '#2B2B2B')   #Content frame
            container_frame.place(x = 50,y = 80)


            #================================================================ Heading ===========================================================#

            frame=Frame(Mod,width=700,height=60,bg='#2B2B2B')  
            frame.place(x=50,y=100)

            heading=Label(frame,text="Difficulty : Moderate",fg='White',bg='#2B2B2B',font=('Calibri',25))
            heading.place(x=25,y=10)



            img = Image.open("C:/Tkinter/Question mark.png")    #image opening
            resize_image = img.resize((20,20)) #resizing image
            tk_img = ImageTk.PhotoImage(resize_image)     #displaying resized image
            label = Label(Mod, image = tk_img, bg = '#2B2B2B')  #image cackround color
            label.place(relx=0.08, rely=0.22)


            #================================================================ END OF Heading ===========================================================#
           

            ques_num=Frame(Mod,width=500,height=25,bg='#2B2B2B')  #Question Number frame
            ques_num.place(x=100,y=172)



            frame2=Frame(Mod,width=850,height=50,bg='#2B2B2B')  #Question displaying frame
            frame2.place(x=50,y=225)


            ans = Frame(container_frame,width=850,height=250,bg='#2B2B2B')
            ans.place(x=0,y=200)



            #================================================================ Printing first question and q.no ===========================================================#



            def on_click_opt1():
                global selected_ans
                opt_1.config(bg = "#02A9F3")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_1["text"][4:]


            def on_click_opt2():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#02A9F3")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_2["text"][4:]
               


            def on_click_opt3():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#02A9F3")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_3["text"][4:]
                


            def on_click_opt4():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#02A9F3")
                selected_ans = opt_4["text"][4:]


            def check_answer():
                global selected_ans,user_score
                if selected_ans == correct_ans[i - 1]:
                    user_score += 1
                    print("Your Score",user_score)
                
                


            q_number=Label(ques_num,text=f"Question {i + 1} of {len(questions)}",fg='White',bg='#2B2B2B',font=('Segoe UI Symbol',11))
            q_number.place(x=0,y=0)

             
                
            heading2=Label(frame2,text=f" {i + 1} ) {questions[0]}",fg='white',bg='#2B2B2B',font=('Arial',16))
            heading2.place(x=23,y=1)


            opt1=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt1.place(x=35,y=8)

            opt2=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt2.place(x=460,y=8)

            opt3=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt3.place(x=35,y=150)

            opt4=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt4.place(x=460,y=150)



            opt1.bind("<Button-1>",on_click_opt1)
            opt2.bind("<Button-1>",on_click_opt2)
            opt3.bind("<Button-1>",on_click_opt3)
            opt4.bind("<Button-1>",on_click_opt4)


            opt_1 = Button(opt1,bg = "#2B2B2B",text = f"a ) {answers[i][0]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt1)
            opt_1.place(x = 0,y = -1)

            opt_2 = Button(opt2,bg = "#2B2B2B",text = f"b ) {answers[i][1]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt2)
            opt_2.place(x = 0,y = -1)

            opt_3 = Button(opt3,bg = "#2B2B2B",text = f"c ) {answers[i][2]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt3)
            opt_3.place(x = 0,y = -1)

            opt_4 = Button(opt4,bg = "#2B2B2B",text = f"d ) {answers[i][3]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt4)
            opt_4.place(x = 0,y = -1)



                



            def question():
                global i,heading2


                def on_click_opt1():
                    global selected_ans
                    opt_1.config(bg = "#02A9F3")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_1["text"][4:]
                    

                def on_click_opt2():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#02A9F3")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_2["text"][4:]

                def on_click_opt3():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#02A9F3")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_3["text"][4:]

                def on_click_opt4():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#02A9F3")
                    selected_ans = opt_4["text"][4:]
              

                if heading2:
                    heading2.destroy()    #To delete the ques on next button

                
                q_number=Label(ques_num,text=f"Question {i + 2} of {len(questions)}",fg='White',bg='#2B2B2B',font=('Segoe UI Symbol',11))
                q_number.place(x=0,y=0)

                if i < len(questions) - 1:
                
                    heading2=Label(frame2,text=f"{i + 2} ) {questions[i + 1]}",fg='white',bg='#2B2B2B',font=('Arial',16))
                    heading2.place(x=23,y=1)

                    opt_1 = Button(opt1,bg = "#2B2B2B",text = f"a ) {answers[i + 1][0]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt1)
                    opt_1.place(x = 0,y = -1)

                    opt_2 = Button(opt2,bg = "#2B2B2B",text = f"b ) {answers[i + 1][1]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt2)
                    opt_2.place(x = 0,y = -1)

                    opt_3 = Button(opt3,bg = "#2B2B2B",text = f"c ) {answers[i + 1][2]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt3)
                    opt_3.place(x = 0,y = -1)

                    opt_4 = Button(opt4,bg = "#2B2B2B",text = f"d ) {answers[i + 1][3]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt4)
                    opt_4.place(x = 0,y = -1)


                i += 1


            def scoques():
                question()
                check_answer()
                
                if i > len(questions) - 1:
                    Mod.destroy()
                    
                    scor=Toplevel(screen)
                    scor.title('Score')
                    scor.geometry('963x781')        #canvas aspect ratio
                    scor.configure(bg='#222325')   #Background color
                    scor.resizable(False,False)
                    

                    #container_frame = Frame(scor,width = 850,height = 550,bg = 'red')
                    #container_frame.place(x = 50,y = 20)

                    frame_a=Frame(scor,width=850,height=800,bg='#222325')
                    frame_a.place(x=50,y=85)
                    
                    img1 = Image.open("C:/Tkinter/—Pngtree—beautiful trophy_4541793.png")    #image opening
                    resize_image1 = img1.resize((120,120)) #resizing image
                    tk_img1 = ImageTk.PhotoImage(resize_image1)     #displaying resized image
                    label2 = Label(frame_a, image = tk_img1, bg = '#222325')  #image cackround color
                    label2.place(relx=.45, rely=.33)

                    img2 = Image.open("C:/Tkinter/congrates-removebg-preview.png")    #image opening
                    resize_image2 = img2.resize((500,200)) #resizing image
                    tk_img2 = ImageTk.PhotoImage(resize_image2)     #displaying resized image
                    label3 = Label(frame_a, image = tk_img2, bg = '#222325')  #image cackround color
                    label3.place(relx=.2, rely=0)

                    
                    #con_b=Label(frame_a,text="CONGRAGULATION!!!",fg='yellow',bg='#222325',font=('Extra Bold',30))
                    #con_b.place(x=220,y=40)        

                    con_a=Label(frame_a,text=f"Your Score is  {user_score}",fg='White',bg='#222325',font=('Helvetica',20))
                    con_a.place(x=330,y=200)


                    
                    con_b=Label(frame_a,text="Press the close button[x] on the top of the window to enter the difficulty choosing \npage",fg='Red',bg='#222325',font=('Courier',12))
                    con_b.place(x=0,y=500)
                    scor.mainloop()




            ne_xt = Button(container_frame,bg = "White",text = "Next",fg="Black",command=scoques,height = 2,width = 10,border = 0,font = ('Arial Black',8))
            ne_xt.place(x = 750,y = 450)

            
            
            Mod.mainloop()



        frame2=Frame(screen,width=230,height=400,bg='#222325',highlightbackground="white", highlightcolor="white", highlightthickness=2)  
        frame2.place(x=365,y=240) #Moderate body container
         
        

        frame2.bind("<Enter>", on_enter)
        frame2.bind("<Leave>", on_leave)



        img2 = Image.open("C:/Tkinter/Moderate.png")
        resize_image2 = img2.resize((150, 200)) 
        tk_img2 = ImageTk.PhotoImage(resize_image2)
        label2 = Label(frame2, image = tk_img2, bg = '#222325')  #image Backround color
        label2.place(relx=0.16, rely=0.05)



        heading2=Label(frame2,text="MODERATE",fg='white',bg='#222325',font=('Courier',16))
        heading2.place(x=60,y=10)

        abt3=Label(frame2,text="Python is a programming \nlanguage that lets you work\n quickly and integrate systems\n more effectively.",fg='white',bg='#222325',font=('Bahnschrift Light',10))
        abt3.place(x=30,y=190)


        button2 = Button(frame2,width=20,pady=7,text = "Let's Begin",bg = '#2B2B2B',fg = 'white',border = 0,relief="groove",font=('Bahnschrift Bold',12),command = Moderate_button)
        button2.place(x=20,y = 325) 
        
#======================================================== EASY BODY =========================================================#
        
        def on_enter(event):
            frame.config(bg='#2B2B2B')
            label.config(bg='#2B2B2B')
            heading.config(bg='#2B2B2B')
            abt1.config(bg='#2B2B2B')
            button.config(bg='#80C454')

# Function to change frame color when mouse leaves
        def on_leave(event):
            frame.config(bg='#222325')
            label.config(bg='#222325')
            heading.config(bg='#222325')
            abt1.config(bg='#222325')
            button.config(bg='#2B2B2B')

        

        def Easy_button():
            Easy = Toplevel(screen)
            Easy.title('Easy')
            Easy.geometry('963x781')        #canvas aspect ratio
            Easy.configure(bg='#222325')   #Background color
            Easy.resizable(False,False)

            global heading2,i
            heading2 = None
            i = 0

            
            

            global questions,answers,correct_ans,user_score
            questions = ["What is the extension of python?","Among these options, which one correctly declares variables?","Which of the following is not a valid data type in Python?",
                         "What is the correct syntax to output \"Hello, World\" in Python?","Which of the following is a correct variable assignment in Python?"]
            answers = [['.py','.c','.C','.java'],['1c = "1"','c d = "1"','c@ = "1"','c = 1'],['bool','int','float','int_float'],['print("Hello, World")','echo "Hello, World"','printf("Hello, World")','print(Hello, World)'],
                       ['x := 10','x = 10','let x = 10','int x = 10']]

            correct_ans = ['.py','c = 1','int_float','print("Hello, World")','x = 10']
            global selected_ans
            selected_ans = None
            user_score=0



            container_frame = Frame(Easy,width = 850,height = 550,bg = '#2B2B2B')
            container_frame.place(x = 50,y = 80)


            #================================================================ Heading ===========================================================#

            frame0=Frame(Easy,width=700,height=60,bg='#2B2B2B')  
            frame0.place(x=50,y=100)

            heading=Label(frame0,text="Difficulty : Easy",fg='White',bg='#2B2B2B',font=('Courier New bold',24))
            heading.place(x=25,y=10)



            img = Image.open("C:/Tkinter/Question mark.png")    #image opening
            resize_image = img.resize((20,20)) #resizing image
            tk_img = ImageTk.PhotoImage(resize_image)     #displaying resized image
            label = Label(Easy, image = tk_img, bg = '#2B2B2B')  #image cackround color
            label.place(relx=0.08, rely=0.22)


            #================================================================ END OF Heading ===========================================================#
            

            ques_num=Frame(Easy,width=500,height=25,bg='#2B2B2B')  #Question Number frame
            ques_num.place(x=100,y=172)



            frame2=Frame(Easy,width=850,height=50,bg='#2B2B2B')  #Question displaying frame
            frame2.place(x=50,y=225)


            ans = Frame(container_frame,width=850,height=250,bg='#2B2B2B')
            ans.place(x=0,y=200)



            #================================================================ Printing first question and q.no ===========================================================#



            def on_click_opt1():
                global selected_ans
                opt_1.config(bg = "#02A9F3")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_1["text"][4:]
                return selected_ans


            def on_click_opt2():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#02A9F3")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_2["text"][4:]
               


            def on_click_opt3():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#02A9F3")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_3["text"][4:]
                


            def on_click_opt4():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#02A9F3")
                selected_ans = opt_4["text"][4:]


            def check_answer():
                global selected_ans, user_score
                if selected_ans == correct_ans[i - 1]:
                    user_score += 1
                    print("Your Score", user_score)
                    

            
                
                        

            q_number=Label(ques_num,text=f"Question {i + 1} of {len(questions)}",fg='White',bg='#2B2B2B',font=('Segoe UI Symbol',11))
            q_number.place(x=0,y=0)

             
                
            heading2=Label(frame2,text=f" {i + 1} ) {questions[0]}",fg='white',bg='#2B2B2B',font=('Arial',16))
            heading2.place(x=23,y=1)


            opt1=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt1.place(x=35,y=8)

            opt2=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt2.place(x=460,y=8)

            opt3=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt3.place(x=35,y=150)

            opt4=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt4.place(x=460,y=150)



            opt1.bind("<Button-1>",on_click_opt1)
            opt2.bind("<Button-1>",on_click_opt2)
            opt3.bind("<Button-1>",on_click_opt3)
            opt4.bind("<Button-1>",on_click_opt4)


            opt_1 = Button(opt1,bg = "#2B2B2B",text = f"a ) {answers[i][0]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt1)
            opt_1.place(x = 0,y = -1)

            opt_2 = Button(opt2,bg = "#2B2B2B",text = f"b ) {answers[i][1]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt2)
            opt_2.place(x = 0,y = -1)

            opt_3 = Button(opt3,bg = "#2B2B2B",text = f"c ) {answers[i][2]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt3)
            opt_3.place(x = 0,y = -1)

            opt_4 = Button(opt4,bg = "#2B2B2B",text = f"d ) {answers[i][3]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt4)
            opt_4.place(x = 0,y = -1)


        


    
                



                


            def question():
                global i, heading2


                def on_click_opt1():
                    global selected_ans
                    opt_1.config(bg = "#02A9F3")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_1["text"][4:]
                    

                def on_click_opt2():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#02A9F3")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_2["text"][4:]

                def on_click_opt3():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#02A9F3")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_3["text"][4:]

                def on_click_opt4():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#02A9F3")
                    selected_ans = opt_4["text"][4:]
              

                if heading2:
                    heading2.destroy()

                
                q_number=Label(ques_num,text=f"Question {i + 2} of {len(questions)}",fg='White',bg='#2B2B2B',font=('Segoe UI Symbol',11))
                q_number.place(x=0,y=0)

                if i < len(questions) - 1:
                
                    heading2=Label(frame2,text=f"{i + 2} ) {questions[i + 1]}",fg='white',bg='#2B2B2B',font=('Arial',16))
                    heading2.place(x=23,y=1)

                    opt_1 = Button(opt1,bg = "#2B2B2B",text = f"a ) {answers[i + 1][0]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt1)
                    opt_1.place(x = 0,y = -1)

                    opt_2 = Button(opt2,bg = "#2B2B2B",text = f"b ) {answers[i + 1][1]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt2)
                    opt_2.place(x = 0,y = -1)

                    opt_3 = Button(opt3,bg = "#2B2B2B",text = f"c ) {answers[i + 1][2]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt3)
                    opt_3.place(x = 0,y = -1)

                    opt_4 = Button(opt4,bg = "#2B2B2B",text = f"d ) {answers[i + 1][3]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt4)
                    opt_4.place(x = 0,y = -1)


                i += 1
            
            def scoques():
                question()
                check_answer()

                
                if i > len(questions) - 1:
                    Easy.destroy()
                    scor=Toplevel(screen)
                    scor.title('Score')
                    scor.geometry('963x781')        #canvas aspect ratio
                    scor.configure(bg='#222325')   #Background color
                    scor.resizable(False,False)

                    #container_frame = Frame(scor,width = 850,height = 550,bg = 'red')
                    #container_frame.place(x = 50,y = 20)

                    frame_a=Frame(scor,width=850,height=800,bg='#222325')
                    frame_a.place(x=50,y=85)
                    
                    img1 = Image.open("C:/Tkinter/—Pngtree—beautiful trophy_4541793.png")    #image opening
                    resize_image1 = img1.resize((120,120)) #resizing image
                    tk_img1 = ImageTk.PhotoImage(resize_image1)     #displaying resized image
                    label2 = Label(frame_a, image = tk_img1, bg = '#222325')  #image cackround color
                    label2.place(relx=.45, rely=.33)

                    img2 = Image.open("C:/Tkinter/congrates-removebg-preview.png")    #image opening
                    resize_image2 = img2.resize((500,200)) #resizing image
                    tk_img2 = ImageTk.PhotoImage(resize_image2)     #displaying resized image
                    label3 = Label(frame_a, image = tk_img2, bg = '#222325')  #image cackround color
                    label3.place(relx=.2, rely=0)

                    
                    #con_b=Label(frame_a,text="CONGRAGULATION!!!",fg='yellow',bg='#222325',font=('Extra Bold',30))
                    #con_b.place(x=220,y=40)        

                    con_a=Label(frame_a,text=f"Your Score is  {user_score}",fg='White',bg='#222325',font=('Helvetica',20))
                    con_a.place(x=330,y=200)


                    
                    con_b=Label(frame_a,text="Press the close button[x] on the top of the window to enter the difficulty choosing \npage",fg='Red',bg='#222325',font=('Courier',12))
                    con_b.place(x=0,y=500)
                    
                    scor.mainloop()

                    


                    
                    


            

            ne_xt = Button(container_frame,bg = "White",text = "Next",fg="Black",command=scoques,height = 2,width = 10,border = 0,font = ('Arial Black',8))
            ne_xt.place(x = 750,y = 450)


        
            
            Easy.mainloop()



        frame=Frame(screen,width=230,height=400,bg='#222325',highlightbackground="white", highlightcolor="white", highlightthickness=2)  
        frame.place(x=70,y=240)
        button = Button(frame,width=20,pady=7,text = "Let's Begin",bg = '#2B2B2B',fg = 'white',border = 0,relief="groove",font=('Bahnschrift Bold',12),command =  Easy_button)
        button.place(x=20,y = 325)


        frame.bind("<Enter>", on_enter)
        frame.bind("<Leave>", on_leave)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)



        img1 = Image.open("C:/Tkinter/Easy.png")
        resize_image = img1.resize((150, 200)) 
        tk_img = ImageTk.PhotoImage(resize_image)


        label = Label(frame, image = tk_img, bg = '#222325')  #image Backround color
        label.place(relx=0.16, rely=0.05)

        heading=Label(frame,text="EASY",fg='white',bg='#222325',font=('Courier',16))
        heading.place(x=80,y=10)

        abt1=Label(frame,text="Python is the best language\n for beginners because \nit's easy to learn and use.",fg='white',bg='#222325',font=('Bahnschrift Light',10))
        abt1.place(x=30,y=190)

       
        
        
        

        
            




#======================================================== DIFFICULT BODY =========================================================#

        def on_enter(event):
            frame1.config(bg='#2B2B2B')
            label1.config(bg='#2B2B2B')
            heading1.config(bg='#2B2B2B')
            abt2.config(bg='#2B2B2B')
            button1.config(bg='#80C454')

# Function to change frame color when mouse leaves
        def on_leave(event):
            frame1.config(bg='#222325')
            label1.config(bg='#222325')
            heading1.config(bg='#222325')
            abt2.config(bg='#222325')
            button1.config(bg='#2B2B2B')


        def diff_button():
            diff=Toplevel(screen)
            diff.title('Question')
            diff.geometry('963x781')        #canvas aspect ratio
            diff.configure(bg='#222325')   #Background color
            diff.resizable(False,False)

            global questions,answers,correct_ans, user_score
            questions = ["Which of the following is not a valid Python data type?","What is the correct way to open a file named \"data.txt\" for reading in Python?","What does the range() function in Python return?",
                         "Python supports the creation of anonymous functions at runtime,\n using a construct called",'Which one of the following is not a keyword in Python language?']
            answers = [['int','char','float','str'],['file = open("data.txt", "r")','file = open("data.txt", "w")',
                                                     'file = open("data.txt", "a")','file = open("data.txt", "rb")'],['A list of numbers',' A tuple of numbers','A generator object',' An iterator object'],['pi','anonymous','lambda','none of the mentioned'],['pass','eval','assert','nonlocal']]


            correct_ans = ['char','file = open("data.txt", "r")','A generator object','lambda','eval']
            global selected_ans
            selected_ans = None
            user_score=0

            global heading2,i
            heading2 = None
            i = 0

            container_frame = Frame(diff,width = 850,height = 550,bg = '#2B2B2B')
            container_frame.place(x = 50,y = 80)


            #================================================================ Heading ===========================================================#

            frame=Frame(diff,width=700,height=60,bg='#2B2B2B')  
            frame.place(x=50,y=100)

            heading=Label(frame,text="Difficulty : Difficult",fg='White',bg='#2B2B2B',font=('Courier New bold',24))
            heading.place(x=25,y=10)



            img = Image.open("C:/Tkinter/Question mark.png")    #image opening
            resize_image = img.resize((20,20)) #resizing image
            tk_img = ImageTk.PhotoImage(resize_image)     #displaying resized image
            label = Label(diff, image = tk_img, bg = '#2B2B2B')  #image cackround color
            label.place(relx=0.08, rely=0.22)


            #================================================================ END OF Heading ===========================================================#
            

            ques_num=Frame(diff,width=500,height=25,bg='#2B2B2B')  #Question Number frame
            ques_num.place(x=100,y=172)



            frame2=Frame(diff,width=850,height=50,bg='#2B2B2B')  #Question displaying frame
            frame2.place(x=50,y=225)


            ans = Frame(container_frame,width=850,height=250,bg='#2B2B2B')
            ans.place(x=0,y=200)



            #================================================================ Printing first question and q.no ===========================================================#



            def on_click_opt1():
                global selected_ans
                opt_1.config(bg = "#02A9F3")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_1["text"][4:]


            def on_click_opt2():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#02A9F3")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_2["text"][4:]
               


            def on_click_opt3():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#02A9F3")
                opt_4.config(bg = "#2B2B2B")
                selected_ans = opt_3["text"][4:]
                


            def on_click_opt4():
                global selected_ans
                opt_1.config(bg = "#2B2B2B")
                opt_2.config(bg = "#2B2B2B")
                opt_3.config(bg = "#2B2B2B")
                opt_4.config(bg = "#02A9F3")
                selected_ans = opt_4["text"][4:]


            def check_answer():
                global selected_ans,user_score
                if selected_ans == correct_ans[i - 1]:
                    user_score += 1
                    print("Your Score",user_score)
                
                


            q_number=Label(ques_num,text=f"Question {i + 1} of {len(questions)}",fg='White',bg='#2B2B2B',font=('Segoe UI Symbol',11))
            q_number.place(x=0,y=0)

             
                
            heading2=Label(frame2,text=f" {i + 1} ) {questions[0]}",fg='white',bg='#2B2B2B',font=('Arial',16))
            heading2.place(x=23,y=1)


            opt1=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt1.place(x=35,y=8)

            opt2=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt2.place(x=460,y=8)

            opt3=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt3.place(x=35,y=150)

            opt4=Frame(ans,bg='#2B2B2B',width = 343,height = 50,highlightbackground="white", highlightcolor="white", highlightthickness=2)
            opt4.place(x=460,y=150)



            opt1.bind("<Button-1>",on_click_opt1)
            opt2.bind("<Button-1>",on_click_opt2)
            opt3.bind("<Button-1>",on_click_opt3)
            opt4.bind("<Button-1>",on_click_opt4)


            opt_1 = Button(opt1,bg = "#2B2B2B",text = f"a ) {answers[i][0]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt1)
            opt_1.place(x = 0,y = -1)

            opt_2 = Button(opt2,bg = "#2B2B2B",text = f"b ) {answers[i][1]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt2)
            opt_2.place(x = 0,y = -1)

            opt_3 = Button(opt3,bg = "#2B2B2B",text = f"c ) {answers[i][2]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt3)
            opt_3.place(x = 0,y = -1)

            opt_4 = Button(opt4,bg = "#2B2B2B",text = f"d ) {answers[i][3]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt4)
            opt_4.place(x = 0,y = -1)



                



            def question():
                global i,heading2
                
                


                def on_click_opt1():
                    global selected_ans
                    opt_1.config(bg = "#02A9F3")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_1["text"][4:]
                    

                def on_click_opt2():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#02A9F3")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_2["text"][4:]

                def on_click_opt3():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#02A9F3")
                    opt_4.config(bg = "#2B2B2B")
                    selected_ans = opt_3["text"][4:]

                def on_click_opt4():
                    global selected_ans
                    opt_1.config(bg = "#2B2B2B")
                    opt_2.config(bg = "#2B2B2B")
                    opt_3.config(bg = "#2B2B2B")
                    opt_4.config(bg = "#02A9F3")
                    selected_ans = opt_4["text"][4:]
              

                if heading2:
                    heading2.destroy()

                
                q_number=Label(ques_num,text=f"Question {i + 2} of {len(questions)}",fg='White',bg='#2B2B2B',font=('Segoe UI Symbol',11))
                q_number.place(x=0,y=0)

                if i < len(questions) - 1:
                
                    heading2=Label(frame2,text=f"{i + 2} ) {questions[i + 1]}",fg='white',bg='#2B2B2B',font=('Arial',16))
                    heading2.place(x=23,y=1)

                    opt_1 = Button(opt1,bg = "#2B2B2B",text = f"a ) {answers[i + 1][0]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt1)
                    opt_1.place(x = 0,y = -1)

                    opt_2 = Button(opt2,bg = "#2B2B2B",text = f"b ) {answers[i + 1][1]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt2)
                    opt_2.place(x = 0,y = -1)

                    opt_3 = Button(opt3,bg = "#2B2B2B",text = f"c ) {answers[i + 1][2]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt3)
                    opt_3.place(x = 0,y = -1)

                    opt_4 = Button(opt4,bg = "#2B2B2B",text = f"d ) {answers[i + 1][3]}",fg="white",width = 37,height = 2,font=('Arial',13),border = 0,activebackground="#2B2B2B",command = on_click_opt4)
                    opt_4.place(x = 0,y = -1)


                i += 1

            def scoques():
                question()
                check_answer()
                
                if i > len(questions) - 1:
                    diff.destroy()
                    scor=Toplevel(screen)
                    scor.title('Score')
                    scor.geometry('963x781')        #canvas aspect ratio
                    scor.configure(bg='#222325')   #Background color
                    scor.resizable(False,False)

                    #container_frame = Frame(scor,width = 850,height = 550,bg = 'red')
                    #container_frame.place(x = 50,y = 20)

                    frame_a=Frame(scor,width=850,height=800,bg='#222325')
                    frame_a.place(x=50,y=85)
                    
                    img1 = Image.open("C:/Tkinter/—Pngtree—beautiful trophy_4541793.png")    #image opening
                    resize_image1 = img1.resize((120,120)) #resizing image
                    tk_img1 = ImageTk.PhotoImage(resize_image1)     #displaying resized image
                    label2 = Label(frame_a, image = tk_img1, bg = '#222325')  #image cackround color
                    label2.place(relx=.45, rely=.33)

                    img2 = Image.open("C:/Tkinter/congrates-removebg-preview.png")    #image opening
                    resize_image2 = img2.resize((500,200)) #resizing image
                    tk_img2 = ImageTk.PhotoImage(resize_image2)     #displaying resized image
                    label3 = Label(frame_a, image = tk_img2, bg = '#222325')  #image cackround color
                    label3.place(relx=.2, rely=0)

                    
                    #con_b=Label(frame_a,text="CONGRAGULATION!!!",fg='yellow',bg='#222325',font=('Extra Bold',30))
                    #con_b.place(x=220,y=40)        

                    con_a=Label(frame_a,text=f"Your Score is  {user_score}",fg='White',bg='#222325',font=('Helvetica',20))
                    con_a.place(x=330,y=200)


                    
                    con_b=Label(frame_a,text="Press the close button[x] on the top of the window to enter the difficulty choosing \npage",fg='Red',bg='#222325',font=('Courier',12))
                    con_b.place(x=0,y=500)
                    
                    scor.mainloop()

        

            ne_xt = Button(container_frame,bg = "White",text = "Next",fg="Black",command=scoques,height = 2,width = 10,border = 0,font = ('Arial Black',8))
            ne_xt.place(x = 750,y = 450)

            diff.mainloop()


        frame1=Frame(screen,width=230,height=400,bg='#222325',highlightbackground="white", highlightcolor="white", highlightthickness=2)  
        frame1.place(x=660,y=240)



        frame1.bind("<Enter>", on_enter)
        frame1.bind("<Leave>", on_leave)



        img1 = Image.open("C:/Tkinter/Difficult.png")
        resize_image1 = img1.resize((150, 200)) 
        tk_img1 = ImageTk.PhotoImage(resize_image1)


        label1 = Label(frame1, image = tk_img1, bg = '#222325')  #image Backround color
        label1.place(relx=0.16, rely=0.05)

        heading1=Label(frame1,text="DIFFICULT",fg='white',bg='#222325',font=('Courier',16))
        heading1.place(x=55,y=10)

        abt2=Label(frame1,text="Python makes us extremely\n productive, and makes \nmaintaining a large and\n rapidly evolving codebase\n relatively simple.",fg='white',bg='#222325',font=('Bahnschrift Light',10))
        abt2.place(x=30,y=190)


        button1 = Button(frame1,width=20,pady=7,text = "Let's Begin",bg = '#2B2B2B',fg = 'white',border = 0,relief="groove",font=('Bahnschrift Bold',12),command = diff_button)
        button1.place(x=20,y = 325)



        screen.mainloop()

    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid","Invalid username and passoword")

    elif password != '1234':
        messagebox.showerror("Invalid","Invalid password")

    elif username != 'admin':
        messagebox.showerror("Invalid","Invalid Username")


        
#======================================================== PYTHON QUIZ HEADING =========================================================#        


frame=Frame(root,width=1000,height=60,bg='#222325')  #Creating frame box login right===========change attribute bg to anyother color to understand
frame.place(x=0,y=50)

heading=Label(frame,text="PYTHON QUIZ",fg='white',bg='#222325',font=('Courier',32,'bold'))  #sign in text
heading.place(x=340,y=8)    #sign in text placement


#======================================================== IMAGE =========================================================#


img = Image.open("C:/Tkinter/coding-languages-removebg-preview (2).png")    #image opening
resize_image = img.resize((500, 500)) #resizing image
tk_img = ImageTk.PhotoImage(resize_image)     #displaying resized image
label = Label(root, image = tk_img, bg = '#222325')  #image cackround color
label.place(relx=0, rely=0.14)   #image postion on canvas


#================================================================================================================#



frame=Frame(root,width=350,height=360,bg='#2B2B2B')  #Creating frame box login right===========change attribute bg to anyother color to understand
frame.place(x=550,y=200)

heading=Label(frame,text="SIGN IN",fg='#57a1f8',bg='#2B2B2B',font=('Arial',23,'bold'))  #sign in text
heading.place(x=110,y=15)    #sign in text placement


#======================================================== USERNAME =========================================================#



def on_enter(e):    #Delete the txt 'usernmae' when user click there
    user.delete(0, 'end') 

def on_leave(e):    #Regenerate the txt 'usernmae' when user go out if it empty
    name = user.get()
    if name == '':
        user.insert(0,'Username')
        
        
user=Entry(frame,width=25,fg='white',border=0,bg='#2B2B2B',font=('Microsoft YaHei UI Light',12))  #inserting textbox
user.place(x=30,y=80)   #placing textbox
user.insert(0,'Username')   #adding 'username' before text box
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width = 295,height = 2,bg = 'white').place(x=25,y=107)  #giving a line below username


#========================================================= PASSWORD ===========================================================#

def on_enter(e):    #Delete the txt 'password' when user click there
    code.delete(0, 'end') 

def on_leave(e):    #Regenerate the txt 'password' when user go out if it is empty
    name = code.get()
    if name == '':
        code.insert(0,'Password')


code=Entry(frame,width=25,fg='white',border=0,bg='#2B2B2B',font=('Microsoft YaHei UI Light',12))  #inserting textbox
code.place(x=30,y=150)   #placing textbox
code.insert(0,'Password')   #adding 'username' before text box
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width = 295,height = 2,bg = 'white').place(x=25,y=177)  #giving a line below username


#========================================================= Sign in Button ===========================================================#

Button(frame,width=39,pady=7,text = 'SIGN IN',bg = '#57a1f8',fg = 'white',border = 0,command = signin).place(x=35,y = 204)   #inserting button
label = Label(frame,text = "Don't have an account?",fg = 'white',bg = '#2B2B2B',font=('Microsoft YaHei UI Light',9))  #Don't have an account text
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text = "Sign Up",border = 0,bg='#2B2B2B',cursor = 'hand2',fg = '#57a1f8')  #Mouse clickk
sign_up.place(x = 215,y = 270)


root.mainloop()

