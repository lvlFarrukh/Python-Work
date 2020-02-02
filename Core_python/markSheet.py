name = input("Enter Name: ")
roll_no = input("Enter Roll No: ")
english_marks = input("Enter English Marks out of 75: ")
urdu_marks = input("Enter Urdu Marks out of 100: ")
maths_marks = input("Enter Mathametics Marks out of 100: ")
chemistry_marks = input("Enter Chemistry Marks out of 100: ")
physics_marks = input("Enter English Marks out of 100: ")

with open("marksheet.txt", "a") as f:

    f.write("\n\n+"+"-"*73+"+"+"\n|"+" "*30+"Mark Sheet"+" "*33+"|\n+"+"-"*73+"+\n")
    f.write("Name: {name}\nRoll No: {roll_no}\n")
    def get_grade(o_m) :
        if o_m <= 100 and o_m >= 80 :
            return "A+"
        if o_m < 80 and o_m >= 70 :
            return "A"
        if o_m < 70 and o_m >= 60 :
            return "B"
        if o_m < 60 and o_m >= 50 :
            return "C"
        if o_m < 50 and o_m >= 40 :
            return "D"
        if o_m < 40 :
            return "F"
    f.write("+"+"-"*20+"+"+"-"*20+"+"+"-"*15+"+"+"-"*15+"+\n")
    f.write("| Subjects"+" "*11+"| Obtain Marks"+" "*7+"| Total Marks"+" "*3+"| Grade"+" "*9+"|\n")
    f.write("+"+"-"*20+"+"+"-"*20+"+"+"-"*15+"+"+"-"*15+"+\n")
    #   Percentage of English
    p_english = (int(english_marks) / 75) * 100
    g_english = get_grade(p_english)
    f.write("| English"+" "*12+f"| {english_marks}"+" "*17+"| 75"+" "*12+f"| {g_english}\n")
    f.write("+"+"-"*20+"+"+"-"*20+"+"+"-"*15+"+"+"-"*15+"+\n")
    #   Percentage of Urdu 
    p_urdu = (int(urdu_marks) / 100) * 100
    g_urdu = get_grade(p_urdu)
    f.write("| Urdu"+" "*15+f"| {urdu_marks}"+" "*17+"| 100"+" "*11+f"| {g_urdu}\n")
    f.write("+"+"-"*20+"+"+"-"*20+"+"+"-"*15+"+"+"-"*15+"+\n")
    #   Percentage of Maths 
    p_maths = (int(maths_marks) / 100) * 100
    g_maths = get_grade(p_maths)
    f.write("| Maths"+" "*14+f"| {maths_marks}"+" "*17+"| 100"+" "*11+f"| {g_maths}\n")
    f.write("+"+"-"*20+"+"+"-"*20+"+"+"-"*15+"+"+"-"*15+"+\n")
    #   Percentage of Chemistry
    p_chemistry = (int(chemistry_marks) / 100) * 100
    g_chemistry = get_grade(p_chemistry)
    f.write("| Chemistry"+" "*10+f"| {chemistry_marks}"+" "*17+"| 100"+" "*11+f"| {g_chemistry}\n")
    f.write("+"+"-"*20+"+"+"-"*20+"+"+"-"*15+"+"+"-"*15+"+\n")
    #   Percentage of Physics
    p_physics = (int(physics_marks) / 100) * 100
    g_physics = get_grade(p_physics)
    f.write("| physics"+" "*12+f"| {physics_marks}"+" "*17+"| 100"+" "*11+f"| {g_physics}\n")
    f.write("+"+"-"*20+"+"+"-"*20+"+"+"-"*15+"+"+"-"*15+"+\n")
    f.write(f"Total Number {int(english_marks)+int(urdu_marks)+int(maths_marks)+int(chemistry_marks)+int(physics_marks)} out of 475\n")
    f.write(f"Total Percentage: {(p_english+p_urdu+p_maths+p_chemistry+p_physics)/5} %\n")
    f.write(f"Grade: {get_grade((p_english+p_urdu+p_maths+p_chemistry+p_physics)/5)}\n")
with open("marksheet.txt", "r") as f:
    print(f.read())



