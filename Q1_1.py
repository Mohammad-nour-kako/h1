graduated_students = ['Mohammad', 'Anas', 'Khaled', 'Ali', 'Osama']
student_name = input('Enter student name:')
for student in graduated_students:
    if student == student_name:
        print('Yes, you are graduated.')
        break
else:
    print('No, you are not graduated.')
