input("Are you Ready for the Kon Baney Ga caror pati:")
print("The Questions now on your Computer Screen")
Question_Answer=[("what is the name of  capital of pakistan:?","Islamabad"),
("What is your name:?","Maria Nadeem"),
("What are your hobies:?","Study and coding"),
("In which Field do you graduated:?","Bs chemistry"),
("How many years you are graduated:?","1 year Before"),
("What's your Father occupation:?","Business"),
("What's your mother occupation:?","House wife")]

for question, answer in Question_Answer:
    input(f"{question}\n")
    print(f"{"Answer of this question is:",answer}")
ans_lst1=["Islamabad"]
ans_lst2=["Maria Nadeem"]
ans_lst3=["Study with practice"]
ans_lst4=["Bs Chemistry"]
ans_lst5=["1 Year"]
ans_lst6=["Business"]
ans_lst7=["House wife"]

# if lst1:
#     print(lst1,ans_lst1)
# elif lst2:
#     print(lst2,ans_lst2)
# elif lst3:
#     print(lst3,ans_lst3)
# elif lst4:
#     print(lst4,ans_lst4)
# elif lst5:
#     print(lst5,ans_lst5)
# elif lst6:
#     print(lst6,ans_lst6)
# else:
#     print(lst7,ans_lst7)

ready = input("Are you ready for 'Kon Baney Ga Caror Pati'? ")

if ready.lower() == "yes":
    questions = [
        "What is the capital of Pakistan?",
        "What is your name?",
        "What are your hobbies?",
        "In which field did you graduate?",
        "How many years did you study for your degree?",
        "What is your father's occupation?",
        "What is your mother's occupation?"
    ]

    answers = [
        "Islamabad",
        "Maria Nadeem",
        "Study with practice",
        "Bs Chemistry",
        "1 Year",
        "Business",
        "Housewife"
    ]

    for i in range(len(questions)):
        input(f"Question {i+1}: {questions[i]} ")
        print(f"Answer: {answers[i]}")
        print()  # Blank line for separation
else:
    print("Alright, maybe next time!")

print("Are you Ready for the Kon Baney Ga caror pati:")
input()  # Wait for user input

print("The Questions now on your Computer Screen")

# Define questions and answers as tuples in a list
questions_answers = [
    ("what is the name of capital of pakistan?", "Islamabad"),
    ("What is your name?", "Maria Nadeem"),
    ("What are your hobbies?", "Study with practice"),
    ("In which Field what's your Graduation?", "Bs Chemistry"),
    ("How many years you are graduated?", "1 Year"),
    ("What's your Father occupation?", "Business"),
    ("What's your mother occupation?", "House wife")
]

# # Iterate through each question-answer pair
# for question, answer in questions_answers:
#     input(f"{question}\n")
#     print(f"Answer: {answer}\n")

# print(input("Are you Ready for the Kon Baney Ga caror pati:"))
# print("The Questions now on your Computer Screen")
# lst1=["what is the name of  capital of pakistan:"],
# lst2=["What is your name:"],
# lst3=["What are your hobies:"],
# lst4=["In which Field what's your Graduation:"],
# lst5=["How many years you are graduated:"],
# lst6=["What's your Father occupation:"]
# lst7=["What's your mother occupation:"]

