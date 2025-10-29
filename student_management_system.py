students = []

VALID_COURSES = ["CSE", "ECE", "IT", "MECH", "CIVIL"]

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("         STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("="*50)

def get_next_student_id(students):
    """Generate next available student ID"""
    if not students:
        return 1
    return max(student["id"] for student in students) + 1

def validate_course(course):
    """Validate if course is from allowed list"""
    return course.upper() in VALID_COURSES

def validate_marks(marks):
    """Validate marks (0-100)"""
    try:
        marks_int = int(marks)
        return 0 <= marks_int <= 100
    except ValueError:
        return False

def add_student(students):
    """Add a new student to the system"""
    print("\n--- Add New Student ---")
    
    if len(students) >= 8:
        print(" Maximum student limit reached (8 students)")
        print("Please delete a student before adding a new one.")
        return students
    
    try:
        print(f"Student ID will be auto-generated: {get_next_student_id(students)}")
        
        name = input("Enter student name: ").strip()
        if not name:
            print(" Name cannot be empty")
            return students
        
        print("\nAvailable Courses: CS, ECE, IT, MECH, CIVIL")
        course = input("Enter course: ").strip().upper()
        if not validate_course(course):
            print(" Invalid course. Please choose from: CS, ECE, IT, MECH, CIVIL")
            return students
        
        marks = input("Enter marks (0-100): ").strip()
        if not validate_marks(marks):
            print(" Invalid marks. Please enter a number between 0-100")
            return students
        
        marks_int = int(marks)
            
    except ValueError:
        print(" Invalid input format")
        return students
    
    new_student = {
        "id": get_next_student_id(students),
        "name": name,
        "course": course,
        "marks": marks_int
    }
    
    students.append(new_student)
    print(f" Student '{name}' added successfully!")
    print(f" Total students: {len(students)}/8")
    
    return students

def view_students(students):
    """Display all students in tabular format"""
    print("\n--- All Students ---")
    
    if not students:
        print(" No students found in the system")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<5} {'Name':<15} {'Course':<8} {'Marks':<8} {'Grade':<8}")
    print("-" * 70)
    
    for student in students:
        if student['marks'] >= 90:
            grade = "A+"
        elif student['marks'] >= 80:
            grade = "A"
        elif student['marks'] >= 70:
            grade = "B"
        elif student['marks'] >= 60:
            grade = "C"
        elif student['marks'] >= 50:
            grade = "D"
        else:
            grade = "F"
        
        print(f"{student['id']:<5} {student['name']:<15} {student['course']:<8} {student['marks']:<8} {grade:<8}")
    
    print("=" * 70)
    print(f" Total Students: {len(students)}/8")

def search_student(students):
    """Search student by ID or Name"""
    print("\n--- Search Student ---")
    
    if not students:
        print(" No students to search")
        return
    
    print("Search by:")
    print("1. Student ID")
    print("2. Student Name")
    
    try:
        search_type = int(input("Enter your choice (1-2): "))
    except ValueError:
        print(" Please enter a valid number")
        return
    
    if search_type == 1:
        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print(" Please enter a valid ID number")
            return
        
        found = False
        for student in students:
            if student["id"] == student_id:
                print("\n Student Found:")
                print("-" * 40)
                print(f"ID: {student['id']}")
                print(f"Name: {student['name']}")
                print(f"Course: {student['course']}")
                print(f"Marks: {student['marks']}")
                
                if student['marks'] >= 90:
                    grade = "A+"
                elif student['marks'] >= 80:
                    grade = "A"
                elif student['marks'] >= 70:
                    grade = "B"
                elif student['marks'] >= 60:
                    grade = "C"
                elif student['marks'] >= 50:
                    grade = "D"
                else:
                    grade = "F"
                print(f"Grade: {grade}")
                print("-" * 40)
                found = True
                break
        
        if not found:
            print(" Student not found with the given ID")
    
    elif search_type == 2:
        name = input("Enter student name: ").strip().lower()
        
        found_students = [student for student in students if name in student["name"].lower()]
        
        if found_students:
            print(f"\n Found {len(found_students)} student(s):")
            print("=" * 60)
            for student in found_students:
                print(f"ID: {student['id']}, Name: {student['name']}, Course: {student['course']}, Marks: {student['marks']}")
            print("=" * 60)
        else:
            print(" No students found with the given name")
    
    else:
        print(" Invalid choice. Please select 1 or 2")

def update_student(students):
    """Update student details"""
    print("\n--- Update Student ---")
    
    if not students:
        print(" No students to update")
        return students
    
    view_students(students)
    
    try:
        student_id = int(input("\nEnter student ID to update: "))
    except ValueError:
        print(" Please enter a valid ID number")
        return students
    
    student_to_update = None
    for student in students:
        if student["id"] == student_id:
            student_to_update = student
            break
    
    if not student_to_update:
        print(" Student not found with the given ID")
        return students
    
    print(f"\nCurrent details of {student_to_update['name']}:")
    print(f"1. Course: {student_to_update['course']}")
    print(f"2. Marks: {student_to_update['marks']}")
    
    print("\nWhat would you like to update?")
    print("1. Course")
    print("2. Marks")
    print("3. Cancel update")
    
    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print(" Please enter a valid number")
        return students
    
    if choice == 1:
        print("\nAvailable Courses: CS, ECE, IT, MECH, CIVIL")
        new_course = input("Enter new course: ").strip().upper()
        if validate_course(new_course):
            student_to_update["course"] = new_course
            print(" Course updated successfully!")
        else:
            print(" Invalid course. Please choose from: CS, ECE, IT, MECH, CIVIL")
    
    elif choice == 2:
        try:
            new_marks = int(input("Enter new marks (0-100): "))
            if 0 <= new_marks <= 100:
                student_to_update["marks"] = new_marks
                print(" Marks updated successfully!")
            else:
                print(" Marks must be between 0-100")
        except ValueError:
            print(" Please enter a valid number for marks")
    
    elif choice == 3:
        print(" Update cancelled")
    
    else:
        print(" Invalid choice")
    
    return students

def delete_student(students):
    """Delete a student by ID"""
    print("\n--- Delete Student ---")
    
    if not students:
        print(" No students to delete")
        return students
    
    view_students(students)
    
    try:
        student_id = int(input("\nEnter student ID to delete: "))
    except ValueError:
        print(" Please enter a valid ID number")
        return students
    
    student_to_delete = None
    for student in students:
        if student["id"] == student_id:
            student_to_delete = student
            break
    
    if not student_to_delete:
        print(" Student not found with the given ID")
        return students
    
    print(f"\n  Are you sure you want to delete {student_to_delete['name']} (ID: {student_to_delete['id']})?")
    print(f"Course: {student_to_delete['course']} | Marks: {student_to_delete['marks']}")
    confirmation = input("Type 'YES' to confirm deletion: ").strip().upper()
    
    if confirmation == "YES":
        students = [student for student in students if student["id"] != student_id]
        print(f" Student '{student_to_delete['name']}' deleted successfully!")
        print(f" Remaining students: {len(students)}/8")
    else:
        print(" Deletion cancelled")
    
    return students

def display_statistics(students):
    """Display student statistics"""
    print("\n--- Student Statistics ---")
    
    if not students:
        print(" No students in the system")
        return
    
    total_students = len(students)
    total_marks = sum(student['marks'] for student in students)
    average_marks = total_marks / total_students
    
    course_dist = {}
    for student in students:
        course = student['course']
        course_dist[course] = course_dist.get(course, 0) + 1
    
    grade_dist = {"A+": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student in students:
        marks = student['marks']
        if marks >= 90:
            grade_dist["A+"] += 1
        elif marks >= 80:
            grade_dist["A"] += 1
        elif marks >= 70:
            grade_dist["B"] += 1
        elif marks >= 60:
            grade_dist["C"] += 1
        elif marks >= 50:
            grade_dist["D"] += 1
        else:
            grade_dist["F"] += 1
    
    highest = max(students, key=lambda x: x['marks'])
    lowest = min(students, key=lambda x: x['marks'])
    
    print(f" Total Students: {total_students}/8")
    print(f" Average Marks: {average_marks:.2f}")
    print(f" Highest Marks: {highest['name']} - {highest['marks']} ({highest['course']})")
    print(f" Lowest Marks: {lowest['name']} - {lowest['marks']} ({lowest['course']})")
    
    print("\n Course Distribution:")
    for course, count in course_dist.items():
        percentage = (count / total_students) * 100
        print(f"   {course}: {count} student(s) ({percentage:.1f}%)")
    
    print("\n Grade Distribution:")
    for grade, count in grade_dist.items():
        if count > 0:
            percentage = (count / total_students) * 100
            print(f"   {grade}: {count} student(s) ({percentage:.1f}%)")

def add_sample_data(students):
    """Add sample student data for testing"""
    sample_students = [
        {"id": 1, "name": "Ravi Kumar", "course": "CS", "marks": 85},
        {"id": 2, "name": "Priya Sharma", "course": "ECE", "marks": 92},
        {"id": 3, "name": "Amit Patel", "course": "IT", "marks": 78},
        {"id": 4, "name": "Sneha Reddy", "course": "MECH", "marks": 65},
        {"id": 5, "name": "Kiran Singh", "course": "CIVIL", "marks": 88}
    ]
    
    for student in sample_students:
        if len(students) < 8:
            students.append(student)
    
    print(" Sample student data added for testing")
    return students

def menu():
    """Main menu function to handle user interactions"""
    global students
    
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print(" Please enter a valid number (1-6)")
            continue
        
        if choice == 1:
            students = add_student(students)
        
        elif choice == 2:
            view_students(students)
            display_statistics(students)
        
        elif choice == 3:
            search_student(students)
        
        elif choice == 4:
            students = update_student(students)
        
        elif choice == 5:
            students = delete_student(students)
        
        elif choice == 6:
            print("\n Thank you for using Student Management System!")
            print(f" Final student count: {len(students)}/8")
            display_statistics(students)
            print("Goodbye! ")
            break
        
        else:
            print(" Invalid choice. Please select 1-6")

if __name__ == "__main__":
    print(" Student Management System")
    print(" Maximum capacity: 8 students")
    print(" Valid Courses: CS, ECE, IT, MECH, CIVIL")
    print(" No data persistence - all data lost on exit")
    
    menu()