from question_model import Question 
from data import question_data 
from quiz_brain import QuizBrain 
question_bank=[]
for q in question_data:
    qstn=q["text"]
    ans=q["answer"]
    new_q=Question(qstn,ans)
    question_bank.append(new_q)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_qstn()
print("You've Completed the quiz")
print(f"Your final score wsa: {quiz.count}/{quiz.q_no}")