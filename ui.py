from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """This class is responsible for ui"""

    #    means specificing a data type of argument
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzleer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score:0", font=("Arial", 18, "normal"), fg="white", bg=THEME_COLOR, pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=400, bg="white")
        self.question_text = self.canvas.create_text(200, 125, text="Question", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=380)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        # self.canvas.create_image(100,300,image=self.true_img)
        # self.canvas.grid(row=2,column=0)
        self.true_button = Button(image=true_img, command=self.true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, command=self.false)
        self.false_button.grid(row=2, column=1)
        self.get_nextquestion()
        self.window.mainloop()

    def get_nextquestion(self):
        """fetch a question"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached at the end of a quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)
        # self.get_nextquestion()

    def false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)


    def give_feedback(self, isright):
        if isright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nextquestion)
