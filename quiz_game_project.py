import quiz_database as quiz

# Sort of Decorative aspects
print("*****************************")
print("Welcome to my Quize Game!!!")


score = 0
def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False
for question_num in range(len(quiz.question_bank)):
    print("*****************************\n")
    print(quiz.question_bank[question_num]["text"]) # Subscript 
    for i in quiz.options[question_num]:
        print(i)
        
    guess = input("Enter your answer(A/B/C/D): ").upper()
    is_correct = check_answer(guess, quiz.question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {quiz.question_bank[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")
    
print("xoxoxoxoxoxoxo THE END xoxoxoxoxoxoxo")
print(f"\nYou have given {score} correct answers")
print(f"Your score is {(score/len(quiz.question_bank)) * 100}%")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        