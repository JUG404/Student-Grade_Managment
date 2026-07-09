student_dictionary = {}

def save_dictionary():
     with open("grades.txt", "w+") as file:
            for student_id in student_dictionary:
                name = student_dictionary[student_id]["name"]
                grade = student_dictionary[student_id]["grade"]
                file.write(f"{student_id}, {name}, {grade}\n")  

def load_dictionary():
    with open("grades.txt", "r") as file:
        for line in file:
            student_id, name, grade = [x.strip() for x in line.split(",")]
            student_dictionary[student_id] = {
                "name": name,
                "grade": int(grade)
            }   
            
def append_record():
    create_backup_file()
    with open("grades.txt", "a") as file:
        new_ID = input("Enter a new student ID: ")
        new_name = input("Enter the new student's name: ")
        new_grade = int(input("Enter the new student's grade: "))
        file.write(f"{new_ID}, {new_name}, {new_grade}\n")#1 appending new record to file
    print("Record added succesfully.")
    load_dictionary()

def  read_dictionary():
    load_dictionary()
    for student_id in student_dictionary:
        print(student_id,
              student_dictionary[student_id]["name"],
              student_dictionary[student_id]["grade"])#2 view all students (read and display all records)  

def search_student():
    load_dictionary()
    search_by = input("Do you want to search by ID or by name? ").lower()
    if search_by == "id" or search_by == "by id":
        get_id = input("Enter student ID: ")
        if get_id in student_dictionary:
            student = student_dictionary[get_id]
            print(f"ID: {get_id}, Name: {student['name']}, Grade: {student['grade']}")
        if get_id not in student_dictionary:
            print("ID not found.")
            answer = input("Do you want to search again? Enter 'yes' if so: ").lower().strip()
            if answer == "yes":
                return search_student()
            else:
                print("Goodbye!")
    elif search_by == "name" or search_by == "by name":
        get_name = input("Enter name: ").lower().strip()
        for student_id, student in student_dictionary.items():
            if get_name == student["name"].lower().strip():
                print(f"ID: {student_id}, Name: {student['name']}, Grade: {student['grade']}")
                return
        else:              
            print("Name not found.")
            answer = input("Do you want to search again? Enter 'yes' if so: ").lower().strip()
            if answer == "yes":
                return search_student()
            else:
                print("Goodbye!")

def update_grade():
    student_id = input("Enter a student ID: ").strip()
    if student_id in student_dictionary:
        new_grade = int(input("Enter new grade: "))
        student_dictionary[student_id]["grade"] = new_grade
        save_dictionary()
        print(f"Updated student record: {student_id}, {student_dictionary[student_id]['name']}, {student_dictionary[student_id]['grade']}")
    else:
        print("ID not found.")
        answer = input("Do you want to search again? Enter 'yes' if so: ").lower().strip()
        if answer == "yes":
            return update_grade()
        else:
            print("Goodbye!")
    load_dictionary()
    create_backup_file()#4 update a grade 
 
def delete_student():
    load_dictionary()
    create_backup_file()
    student_id = input("Enter the ID of the student whose record you want to delete: ").strip()
    if student_id in student_dictionary:
        student_dictionary.pop(student_id)
        save_dictionary()
        print(f"Student with ID {student_id} has succesfully been deleted. ")
    else:
        print("ID not found.")
        answer = input("Do you want to try again? Enter 'yes' if so: ").lower().strip()
        if answer == "yes":
            return delete_student()
        else:
            print("Goodbye!")#5 delete a student record 

def compute_stats():
    load_dictionary()
    global max_grade, min_grade, total, count
    max_grade = None
    min_grade = None
    total = 0
    count = 0
    for student_id in student_dictionary:
        grade = int(student_dictionary[student_id]["grade"])

        if max_grade is None or grade > max_grade:
            max_grade = grade
        if min_grade is None or grade < min_grade:
            min_grade = grade
        total += grade
        count +=1
    average_grade = total/count
    return (min_grade, max_grade, average_grade)#7 compute highest,lowest,average grade, without printing

def process_stats():   
    min_grade, max_grade, average_grade = compute_stats()
    print(f"Highest grade: {max_grade}")                  
    print(f"Lowest grade: {min_grade}")
    print(f"Average grade: {average_grade}")#prints compute_stats 

def above_avg():
    min_grade, max_grade, average_grade = compute_stats()
    above_average = []
    for student_id in student_dictionary:
        grade = int(student_dictionary[student_id]["grade"])
        if grade > average_grade:
            above_average.append(student_dictionary[student_id]["name"])    
    print(f"Students who scored above the average grade: {above_average}") #display students who scored above average

def below_avg():
    min_grade, max_grade, average_grade = compute_stats()
    below_average = []
    for student_id in student_dictionary:
        grade = int(student_dictionary[student_id]["grade"])
        if grade < average_grade:
            below_average.append(student_dictionary[student_id]["name"])
    print(f"Students who scored below the average grade: {below_average}")#display students who scored below average

def view_students():
    records = []
    with open("grades.txt", "r") as file:
        for line in file:
            student_id, name, grade = line.strip().split(", ")            
            records.append([student_id, name, int(grade)])
    print("Sort by:")
    print("1. ID")
    print("2. Name")
    print("3. Grade")
    choice = input("Choose an option: ")
    if choice == "1":
        records.sort(key=lambda student: student[0])  #id 
    elif choice == "2":
        records.sort(key=lambda student: student[1].lower())  #name

    elif choice == "3":
        records.sort(key=lambda student: student[2])  #grade

    for student in records:
        print(student)#sort by name grade or id  and display

def create_backup_file():
    with open("grades.txt", "r") as file:
        content = file.read()

    with open("backup_grades.txt", "w") as backup_file:
        backup_file.write(content)

    print("Backup file created succesfully.")#9 backup file  

#10 GUI

def main():
    running = True
    while running:    #executes the program continually
        command = input("What action do you want to take (read, append, search, update, delete, sort, stats, above average, below average or exit?) ").strip().lower()
        if command == "read":
            read_dictionary()
        elif command == "append":
            append_record()
        elif command == "search":
            search_student()
        elif command == "update":
            update_grade()
        elif command == "delete":
            delete_student()
        elif command == "sort":
            view_students()
        elif command == "stats":
            process_stats()
        elif command == "above average":
            above_avg()
        elif command == "below average":
            below_avg()
        elif command == "exit":
            print("Exiting application.")
            running = False
        else:  
            print("Choose one of the allowed actions.") 
main()
