class QuizBrain:
    def __init__(self,q_list):
        self.q_no=0
        self.q_list=q_list 
        self.count=0
    def next_qstn(self):
        current_qstn=self.q_list[self.q_no]
        user_ans=input(f"Q.{self.q_no+1}{current_qstn.qstn}(True/False)")
        self.q_no +=1 
        self.check_ans(user_ans,current_qstn.ans)
    def still_has_questions(self):
        return self.q_no < len(self.q_list)
    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower()==correct_ans.lower():
            print("You got it Right!")
            self.count +=1
            
        else:
            print("That's Wrong!")
        print(f"The corrcet answer was:{correct_ans} ")
        print(f"Your current score is:{self.count}/{self.q_no}")
        print("\n")