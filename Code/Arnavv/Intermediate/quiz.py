def quiz():
    quiz_data = [
        ["What is the capital of Nepal?", ["Kathmandu", "Lalitpur", "Biratnagar", "Hetauda"], "a"],
        ["Which programming language are we using right now?", ["Java", "Python", "C++", "Ruby"], "b"],
        ["What is 5 + 7?", ["10", "11", "12", "13"], "c"],
        ["Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "b"],
        ["Who wrote 'Hamlet'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "J.K. Rowling"], "c"],
    ]
    prizes = ["0", "1,000", "10,000", "50,000", "250,000", "1,000,000"]
    points = 0
 
    for i in quiz_data:
        print(i[0])

        opt = i[1]
        print(f"a) {opt[0]}  b) {opt[1]}  c) {opt[2]}  d) {opt[3]}")
        ans = i[2]
        answer = input("Enter the answer: ")
        if answer == ans:
            print("Correct")
            points += 1
            print(f"Your points: {points}")
        else:
            print("Wrong")
            break
        print("You won", prizes[points])

quiz()