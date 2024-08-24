#   1st Method
questions=[
    ["The Facebook is created by which language:", "python","java","Django","PHP", 4],
    ["Which programming language is primarily used for Android app development:", "Python", "Swift", "Java", 4],
    ["The core language of the iOS operating system is:", "Python", "Java", "Kotlin","Swift", 4],
    ["Which of the following is not a relational database management system:", "MySQL", "PostgreSQL", "SQLite","MongoDB", 4],
    ["Which language is known for its use in data science and machine learning:", "Ruby", "C#", "JavaScript","Python",  4],
    ["Which of these is a front-end web development framework:", "Django", "Flask",  "Laravel", "Angular", 4],
    ["Which of these is not a programming language:", "JavaScript", "Python", "C++", "HTML", 4],
    ["Which language is primarily used for server-side scripting:", "JavaScript", "Ruby", "Perl","PHP", 4],
    ["What is the main language used for writing scripts in Unity game engine:", "JavaScript", "Python", "Swift", "C#", 4],
    ["Which of the following is a NoSQL database:", "PostgreSQL", "Oracle", "SQL Server", "MongoDB", 4],
    ["Which language is known for its role in web development and backend services:", "Python", "JavaScript", "PHP", "JavaScript", 4],
    ["Which of the following is a framework for building cross-platform mobile apps:", "Django", "Spring", "Flask", "React Native",4],
    ["Which language is typically used for writing system-level software:", "Java", "Python", "Ruby", "C", 4],
    ["Which programming language is known for its simplicity and readability:", "Java","C++", "Perl","Python",  4],
    ["Which language is primarily used for statistical analysis and data visualization:", "Python", "Java", "C#", "R", 4],
    ["Which of these languages is not typically used for web development:", "HTML", "JavaScript", "Python", "C++", 4],
    ["Which programming language is known for its use in web browsers:", "Ruby", "Java", "PHP", "JavaScript", 4],
    ["Which of these is a popular JavaScript library for building user interfaces:", "Django", "Flask", "Spring", "React", 4],
    ["Which programming language was developed by Microsoft:", "Java", "Python", "Ruby", "C#", 4],
    ["Which of the following is a lightweight and minimalistic JavaScript framework:", "Angular", "Spring", "Laravel", "Vue.js", 4],
    ["Which language is known for its strong static typing and use in large-scale applications:", "JavaScript", "Ruby", "PHP", "Java", 4]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0, len(questions)):
    question=questions[i]
    print(f"a.{question[1]}      b.{question[2]}")
    print(f"c.{question[3]}      d.{question[4]}")
    reply=int(input("Enter the option from 1-4 or otherwise quit\n"))
    if reply==0:
        money=levels[i-1]
        break
    if reply==question[-1]:
       print(f"You are now won the RS.{levels[i]}")
    elif i==4:
        money=10000
        print("You are move to the lower at this level as you give the wrong answer:", 10000)
    elif i==4:
        money=32000
        print("Youu are move to the lower at this level as you give the wrong answer:", 32000)
    elif i==9:
        money=10000000
        print("Youu are move to the lower at this level as you give the wrong answer:",100000)
    else:
        print(f"Completely wrong question now you can quit: and you balance is RS.{levels[i]}")
        break
print(f"Congratulations you won the cash of RS.{levels[i]}")


#2nd Method
questions=[
    ["The Facebook is created by which language:", "python","java","Django","PHP", 4],
    ["Which programming language is primarily used for Android app development:", "Python", "Swift", "Java", 4],
    ["The core language of the iOS operating system is:", "Python", "Java", "Kotlin","Swift", 4],
    ["Which of the following is not a relational database management system:", "MySQL", "PostgreSQL", "SQLite","MongoDB", 4],
    ["Which language is known for its use in data science and machine learning:", "Ruby", "C#", "JavaScript","Python",  4],
    ["Which of these is a front-end web development framework:", "Django", "Flask",  "Laravel", "Angular", 4],
    ["Which of these is not a programming language:", "JavaScript", "Python", "C++", "HTML", 4],
    ["Which language is primarily used for server-side scripting:", "JavaScript", "Ruby", "Perl","PHP", 4],
    ["What is the main language used for writing scripts in Unity game engine:", "JavaScript", "Python", "Swift", "C#", 4],
    ["Which of the following is a NoSQL database:", "PostgreSQL", "Oracle", "SQL Server", "MongoDB", 4],
    ["Which language is known for its role in web development and backend services:", "Python", "JavaScript", "PHP", "JavaScript", 4],
    ["Which of the following is a framework for building cross-platform mobile apps:", "Django", "Spring", "Flask", "React Native",4],
    ["Which language is typically used for writing system-level software:", "Java", "Python", "Ruby", "C", 4],
    ["Which programming language is known for its simplicity and readability:", "Java","C++", "Perl","Python",  4],
    ["Which language is primarily used for statistical analysis and data visualization:", "Python", "Java", "C#", "R", 4],
    ["Which of these languages is not typically used for web development:", "HTML", "JavaScript", "Python", "C++", 4],
    ["Which programming language is known for its use in web browsers:", "Ruby", "Java", "PHP", "JavaScript", 4],
    ["Which of these is a popular JavaScript library for building user interfaces:", "Django", "Flask", "Spring", "React", 4],
    ["Which programming language was developed by Microsoft:", "Java", "Python", "Ruby", "C#", 4],
    ["Which of the following is a lightweight and minimalistic JavaScript framework:", "Angular", "Spring", "Laravel", "Vue.js", 4],
    ["Which language is known for its strong static typing and use in large-scale applications:", "JavaScript", "Ruby", "PHP", "Java", 4]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0, len(questions)):
    question=questions[i]
    print(f"a. {question[1]}      b.{question[2]}")
    print(f"a. {question[3]}      b.{question[4]}")
    reply=int(input("Enter the answer otherwise quit \n:"))
    if reply == 0:
        question=question[-1]
        print(f"you won the money {levels[i]}")
        break
    elif reply==4:
        money = 10000
        print(f"Now you won the money {levels[i]}")
    elif reply==9:
        money = 640000
        print(f"Now you won the money {levels[i]}")
    elif reply==14:
        money = 10000000
        print(f"Now you won the money {levels[i]}")
    else:
        print(f"Wrong answer so you get RS.{levels[i]}")
        break
print(f"Congratulations you won RS.{levels[i]}")


         