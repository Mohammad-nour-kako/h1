questions = []
answers = []
f = open('questions_answers.txt')
content = f.read()
lines = content.split('\n')
f.close()

for line in lines:
    q_a = line.split(':')
    questions.append(q_a[0])
    answers.append(q_a[1])

count = len(questions)

name = input('Enter Your name: ')
print('Quiz started.\nFor each question, Please Answer Y or N')
mark = 0

for i in range(count):
    question = questions[i]
    answer = answers[i]
    student_answer = input(question+". (Y or N)? ")
    if student_answer==answer:
        mark+=1

print('Quiz Finished.\nyour mark:', mark,'/',count)

f = open('results.txt', 'a')
f.write(name + " -> " + str(mark) + "/" + str(count) + "\n")
