
# Define a function to calculate total score and overall grade
def calculate_grade(scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)

    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return total_score, grade

# Function to display all students' details
def display_students(students):
    print("\nStudent Details:")
    print(f"{'Name':<20} {'Student ID':<15} {'Total Score':<15} {'Grade'}")
    print("-" * 60)
    for student in students:
        print(f"{student['name']:<20} {student['student_id']:<15} {student['total_score']:<15} {student['grade']}")
    print("-" * 60)

def main():
    students = []

    while True:
        # Gather student information
        name = input("Enter student name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        student_id = input("Enter student ID: ")
        scores = []
        
        for i in range(1, 4):  # Assuming there are 3 subjects
            score = float(input(f"Enter score for subject {i}: "))
            scores.append(score)

        total_score, grade = calculate_grade(scores)

        # Store student data in a dictionary
        student_data = {
            'name': name,
            'student_id': student_id,
            'scores': scores,
            'total_score': total_score,
            'grade': grade
        }
        students.append(student_data)

    # Display all student details
    display_students(students)

if __name__ == "__main__":
    main()
