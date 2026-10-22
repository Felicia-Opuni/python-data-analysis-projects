students = [
    {"name": "Ama", "score": 75},
    {"name": "Kojo", "score": 40},
    {"name": "Abena", "score": 88}
]


def get_grade(score):
    # Grade logic here
    
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Fail"
    
    


def analyze_students(students):
    # Student-analysis logic here
   
    total = 0
    passes = 0
    fails = 0
    

    # Handle an empty student list
    if students == []:
        print("No student records available.")
        return

    highest = students[0]["score"]
    lowest = students[0]["score"]

    for student in students:
        name = student["name"]
        score = student["score"]

       
        
        # Update total
        total += score
        # Count passes and failures
        if score >= 50:
            passes += 1
        else:
            fails += 1

        # Update highest and lowest scores
        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

        # Get this student's grade using your function
        grade = get_grade(score)

        print(name, "| Score:", score, "| Grade:", grade)

        # Calculate class statistics AFTER the loop
    average = total / len(students)
    pass_rate = (passes / len(students) * 100)

    print("\nCLASS SUMMARY")
    print("Total students:", len(students))
    print("Total score:", total)
    print("Average score:", round(average, 2))
    print("Highest score:", highest)
    print("Lowest score:", lowest)
    print("Passes:", passes)
    print("Failures:", fails)
    print("Pass rate:", round(pass_rate, 2), "%")
       
    


# Run the program
analyze_students(students)

